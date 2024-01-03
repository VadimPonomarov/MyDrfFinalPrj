from django.contrib.auth import get_user_model
from django.db import transaction
from django.shortcuts import get_object_or_404, render

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from apps.users.filters import UserFilter
from apps.users.serializers import AccountSerializer, UserSerializer

from core.enums.user_enums import AccountTypeEnum
from core.permissions.user_permissions import IsMeUserPermission, SuperAdminPermission
from core.services.jwt_service import ActivateToken, JWTService
from rest_framework_simplejwt.tokens import Token

UserModel = get_user_model()


class UserListCreateView(ListCreateAPIView):
    http_method_names = ('get', 'post',)
    queryset = UserModel.objects.all().prefetch_related('account')
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = (IsAdminUser,)
        else:
            permission_classes = (AllowAny,)
        return (permission() for permission in permission_classes)


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all().prefetch_related('account')
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = (IsMeUserPermission,)
        else:
            permission_classes = (IsMeUserPermission,)
        return (permission() for permission in permission_classes)


class UserActivateView(GenericAPIView):
    http_method_names = ('get',)
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def get(self, *args, **kwargs):
        token: Token = kwargs.get('token')
        user = JWTService.validate_token(token, ActivateToken)
        user.is_active = True
        user.save()
        return render(self.request, 'index.html')


class UserAccountCRUDView(GenericAPIView):
    queryset = UserModel.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get(self):
        user = self.request.user
        if not user.account:
            return Response("!!! Uou still do not have an account.", status.HTTP_400_BAD_REQUEST)

        account_serialized = AccountSerializer(user.account)
        return Response(account_serialized.data, status.HTTP_200_OK)

    @transaction.atomic
    def post(self, *args, **kwargs):
        user = self.request.user
        if user.account:
            return Response("!!! Forbidden. User already has an account.", status.HTTP_400_BAD_REQUEST)
        account_serializer = AccountSerializer(data=self.request.data)
        account_serializer.is_valid(raise_exception=True)
        account = account_serializer.create(account_serializer.validated_data)
        user.account = account
        user.save()
        user_serialized = self.get_serializer(user)
        return Response(user_serialized.data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        user = self.request.user
        account_serializer = AccountSerializer(data=self.request.data)
        account_serializer.is_valid(raise_exception=True)
        user.account.account_type = account_serializer.validated_data.get('account_type')
        user.account.client_type = account_serializer.validated_data.get('client_type')
        user.save()
        user_serialized = self.get_serializer(user)
        return Response(user_serialized.data, status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        self.put(self, *args, **kwargs)

    def delete(self, *args, **kwargs):
        user = self.request.user
        user.account_id = None
        user.save()
        user_serialized = self.get_serializer(user)
        return Response(user_serialized.data, status.HTTP_200_OK)


class ManageUserAccountsCRUDView(GenericAPIView):
    queryset = UserModel.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer

    def get(self):
        user = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
        if not user.account:
            return Response("!!! The User still has no account.", status.HTTP_400_BAD_REQUEST)

        account_serialized = AccountSerializer(user.account)
        return Response(account_serialized.data, status.HTTP_200_OK)

    @transaction.atomic
    def post(self, *args, **kwargs):
        user = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
        if user.account:
            return Response("!!! Forbidden. User already has an account.", status.HTTP_400_BAD_REQUEST)
        account_serializer = AccountSerializer(data=self.request.data)
        account_serializer.is_valid(raise_exception=True)
        account = account_serializer.create(account_serializer.validated_data)
        user.account = account
        user.save()
        user_serialized = self.get_serializer(user)
        return Response(user_serialized.data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        user = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
        account_serializer = AccountSerializer(data=self.request.data)
        account_serializer.is_valid(raise_exception=True)
        user.account.account_type = account_serializer.validated_data.get('account_type')
        user.account.client_type = account_serializer.validated_data.get('client_type')
        user.save()
        user_serialized = self.get_serializer(user)
        return Response(user_serialized.data, status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        self.put(self, *args, **kwargs)

    def delete(self, *args, **kwargs):
        user = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
        user.account_id = None
        user.save()
        user_serialized = self.get_serializer(user)
        return Response(user_serialized.data, status.HTTP_200_OK)


class UserAccountTypeToggleView(GenericAPIView):
    queryset = UserModel.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [SuperAdminPermission]

    def patch(self, *args, **kwargs):
        user = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
        account = user.account
        if not user.account:
            return Response("User still has no account.", status.HTTP_400_BAD_REQUEST)
        account.account_type = AccountTypeEnum.BASE.value \
            if account.account_type != AccountTypeEnum.BASE.value \
            else AccountTypeEnum.PREMIUM.value
        account.save()
        account_serialized = self.get_serializer(account)
        return Response(account_serialized.data, status.HTTP_200_OK)
