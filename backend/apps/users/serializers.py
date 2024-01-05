import asyncio

from django.contrib.auth import get_user_model
from django.db import transaction

from rest_framework.serializers import ModelSerializer

from apps.users.models import AccountModel

from core.serializers import BaseSerializer
from core.services.email_service import EmailService

UserModel = get_user_model()


class AccountSerializer(ModelSerializer):
    class Meta:
        model = AccountModel
        fields = ('id', 'client_type', 'account_type')


class UserSerializer(BaseSerializer):
    account = AccountSerializer(allow_null=True, required=False)

    class Meta:
        model = UserModel
        fields = ('id', 'email', 'password', 'is_superuser', 'is_active', 'is_staff',
                  'account') + BaseSerializer.Meta.fields
        read_only_fields = ('is_superuser',)
        extra_kwargs = {
            'password': {'write_only': True}
        }

    @transaction.atomic
    def create(self, validated_data: dict):
        if validated_data.get('account'):
            account = validated_data.pop('account')
            account = AccountModel.objects.create(**account)
            user = UserModel.objects.create_user(account=account, **validated_data)
        else:
            user = UserModel.objects.create_user(account=None, **validated_data)
        EmailService.send_register_email(user)
        return user


class UserSerializer_(ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('email',)
