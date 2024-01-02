from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core import validators as V

from core.enums.user_enums import UserRoleEnum, AccountTypeEnum, UserRegEx
from core.models import BaseModel
from .managers import UserManager
from django.db import models


class AccountModel(BaseModel):
    class Meta:
        db_table = 'accounts'
        ordering = ['id']

    client_type = models.CharField(max_length=255, choices=UserRoleEnum.get_choices(), default=UserRoleEnum.SELLER.role)
    account_type = models.CharField(max_length=255, choices=AccountTypeEnum.get_choices(),
                                    default=AccountTypeEnum.BASE.acc_type)


class UserModel(AbstractBaseUser, PermissionsMixin, BaseModel):
    class Meta:
        db_table = 'users'
        ordering = ['id', 'email']

    email = models.EmailField(unique=True, validators=[V.EmailValidator])
    password = models.CharField(max_length=255,
                                validators=[V.RegexValidator(UserRegEx.PASSWORD.pattern, UserRegEx.PASSWORD.msg)])
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    account = models.OneToOneField(AccountModel, on_delete=models.SET_NULL, related_name='user', null=True,
                                   default=None)

    USERNAME_FIELD = 'email'

    objects = UserManager()
