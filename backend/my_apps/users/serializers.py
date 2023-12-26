import time
from multiprocessing import Process

from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from django.db import transaction

from my_apps.users.models import AccountModel
from core.services.email_services import EmailService

UserModel = get_user_model()


class AccountSerializer(ModelSerializer):
    class Meta:
        model = AccountModel
        fields = ('id', 'client_type', 'account_type')


class UserSerializer(ModelSerializer):
    account = AccountSerializer(allow_null=True, required=False)

    class Meta:
        model = UserModel
        fields = ('id', 'email', 'is_superuser', 'is_staff', 'is_active', 'password', 'account',)
        read_only_fields = ('is_superuser', 'is_active', 'is_staff')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    @transaction.atomic
    def create(self, validated_data: dict):
        t = time.time()
        if validated_data.get('account'):
            account = validated_data.pop('account')
            account = AccountModel.objects.create(**account)
            user = UserModel.objects.create_user(account=account, **validated_data)
        else:
            user = UserModel.objects.create_user(account=None, **validated_data)
        Process(EmailService.send_register_email(user)).start()
        return user


class UserSerializer_(ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('email',)
