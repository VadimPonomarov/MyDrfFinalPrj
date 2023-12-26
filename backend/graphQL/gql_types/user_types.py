from django.contrib.auth import get_user_model
from django.db.models import Model

from graphene_django import DjangoObjectType

UserModel: Model = get_user_model()


class UserType(DjangoObjectType):
    class Meta:
        model = UserModel
        fields = '__all__'

    def resolve_password(self, info):
        return '⛔'
