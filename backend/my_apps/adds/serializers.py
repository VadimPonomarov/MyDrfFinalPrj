from rest_framework import serializers

from my_apps.adds.models import AddsModel
from my_apps.catalogs.serializers import CarBrandModelSerializer_, \
    CarBrandSerializer_
from my_apps.users.serializers import UserSerializer_


class AddsSerializer_(serializers.ModelSerializer):
    owner = UserSerializer_(required=False)
    brand = CarBrandSerializer_(required=False)
    model = CarBrandModelSerializer_(required=False)

    class Meta:
        model = AddsModel
        fields = '__all__'


class AddsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddsModel
        fields = '__all__'
