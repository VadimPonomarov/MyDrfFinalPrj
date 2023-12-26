from django.db import models
from django.core import validators as V
from core.enums.common_enums import CarMarkEnum


class CarBrandModel(models.Model):
    class Meta:
        db_table = 'catalog_car_brands'
        ordering = ['id']

    brand = models.CharField(max_length=20, unique=True,
                             validators=[V.MaxLengthValidator(20),
                                         V.RegexValidator(CarMarkEnum.MARK.pattern, CarMarkEnum.MARK.msg)
                                         ])


class CarBrandModelModel(models.Model):
    class Meta:
        db_table = 'catalog_car_brand_models'
        ordering = ['id']

    model_name = models.CharField(max_length=20, unique=True,
                                  validators=[V.MaxLengthValidator(20),
                                              V.RegexValidator(CarMarkEnum.MODEL.pattern, CarMarkEnum.MODEL.msg)
                                              ])
    brand = models.ForeignKey(CarBrandModel, on_delete=models.CASCADE, related_name='car_brand', null=False)


class LocalitiesModel(models.Model):
    class Meta:
        db_table = 'localities'
        ordering = ['id']

    locale_id = models.PositiveIntegerField(blank=False, unique=True)
    type = models.CharField(max_length=20)
    name = models.JSONField()
    public_name = models.JSONField()
    post_code = models.JSONField()
    katottg = models.CharField(max_length=20)
    koatuu = models.CharField(max_length=10)
    lng = models.FloatField(blank=True)
    lat = models.FloatField(blank=True)
    parent_id = models.PositiveIntegerField(blank=False)
