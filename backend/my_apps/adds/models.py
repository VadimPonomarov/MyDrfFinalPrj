from django.contrib.auth import get_user_model
from django.core import validators as V
from django.db import models

from my_apps.catalogs.models import CarBrandModel, CarBrandModelModel

from core.enums.common_enums import CurrenciesEnum
from core.models import BaseModel

UserModel = get_user_model()


class AddsModel(BaseModel):
    class Meta:
        db_table = 'adds'
        ordering = ['id']

    owner = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='user')
    title = models.CharField(max_length=100)
    brand = models.OneToOneField(CarBrandModel, on_delete=models.CASCADE, related_name='brands')
    model = models.OneToOneField(CarBrandModelModel, on_delete=models.CASCADE, related_name='brand_models')
    year = models.PositiveSmallIntegerField()
    price = models.FloatField()
    currency = models.CharField(max_length=3, choices=CurrenciesEnum.get_choices(), default=CurrenciesEnum.UAH.cur)
    description = models.TextField(max_length=300, validators=[V.MaxLengthValidator(300, "Total length must not exceed 300 symbols")])
    