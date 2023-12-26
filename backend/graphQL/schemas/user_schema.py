import os
from concurrent.futures import ThreadPoolExecutor
import graphene
from graphene.types import ResolveInfo
from graphql_jwt.decorators import login_required, staff_member_required
from django.contrib.auth.base_user import BaseUserManager

from core.services.email_services import EmailService
from my_apps.users.serializers import UserSerializer
from ..gql_types import UserModel, UserType


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")
    me = graphene.Field(UserType)
    users = graphene.List(UserType)

    @login_required
    def resolve_me(self, info: ResolveInfo, *args, **kwargs):
        return UserModel.objects.get(email=info.context.user)

    @staff_member_required
    @login_required
    def resolve_users(self, info: ResolveInfo, *args, **kwargs):
        return UserModel.objects.all()


class NewUserMutation(graphene.Mutation):
    class Meta:
        serializer_class = UserSerializer

    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    user = graphene.Field(UserType)

    def mutate(self, info, email, password):
        try:
            email = BaseUserManager.normalize_email(email)
            input_data = dict(email=email, password=password)
            serializer = UserSerializer(data=input_data)
            serializer.is_valid(raise_exception=True)
            validated_data = serializer.validated_data
            new_user = UserModel.objects.create(**validated_data)
            new_user.set_password(password)
            new_user.save()
            with ThreadPoolExecutor(max_workers=os.cpu_count() * 5) as executor:
                executor.submit(EmailService.send_register_email, new_user)
            return NewUserMutation(user=new_user)
        except Exception as err:
            return err


class Mutation(graphene.ObjectType):
    create_user = NewUserMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
