from rest_framework import serializers

from my_apps.catalogs.models import CarBrandModelModel, CarBrandModel, LocalitiesModel


class CarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrandModel
        fields = ('id', 'brand')


class CarBrandSerializer_(serializers.ModelSerializer):
    class Meta:
        model = CarBrandModel
        fields = ('brand',)


class CarBrandModelSerializer(serializers.ModelSerializer):
    brand = CarBrandSerializer(required=False)

    class Meta:
        model = CarBrandModelModel
        fields = ('id', 'model_name', 'brand')


class CarBrandModelSerializer_(serializers.ModelSerializer):
    class Meta:
        model = CarBrandModelModel
        fields = ('model_name',)


class LocalitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalitiesModel
        fields = '__all__'
