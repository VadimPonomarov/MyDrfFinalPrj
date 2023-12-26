from django.contrib.auth import get_user_model
from django.http import HttpResponse
from rest_framework import status, mixins
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView
from werkzeug.sansio.response import Response

from my_apps.adds.models import AddsModel
from my_apps.adds.serializers import AddsSerializer, AddsSerializer_
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.permissions.user_permissions import IsAddOwnerPermission

UserModel = get_user_model()


class AddsListCreateView(mixins.ListModelMixin, GenericAPIView):
    queryset = AddsModel.objects.all()
    serializer_class = AddsSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer(self, *args, **kwargs):
        if self.request.method in ['GET']:
            serializer_class = AddsSerializer_
            kwargs.setdefault('context', self.get_serializer_context())
            return serializer_class(*args, **kwargs)
        else:
            serializer_class = self.get_serializer_class()
            kwargs.setdefault('context', self.get_serializer_context())
            return serializer_class(*args, **kwargs)

    def post(self, *args, **kwargs):
        is_premium = bool("PREMIUM" == UserModel.objects.all()
                          .select_related('account')
                          .get(pk=self.request.user.id)
                          .account.account_type)
        if not is_premium and AddsModel.objects.get(owner_id=self.request.user.id):
            return HttpResponse('!!! Adds limit is exceeded',
                                status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        adds = AddsModel.objects.create(**serializer.validated_data)
        serializer = self.get_serializer(adds)
        return Response(serializer.data, status.HTTP_200_OK)

    def get(self, *args, **kwargs):
        return super().list(self, *args, **kwargs)


class RetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = AddsModel.objects.all()
    serializer_class = AddsSerializer
    permission_classes = [IsAuthenticated, IsAddOwnerPermission]
