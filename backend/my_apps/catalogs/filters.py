from django_filters import rest_framework as filters

from .models import BrandModel, BrandModelModel


class BrandFilter(filters.FilterSet):
    class Meta:
        model = BrandModel
        fields = {
            'id': ['lte', 'gte', 'exact'],
            'car_brand': ['startswith', 'endswith', 'contains'],
        }

    order = filters.OrderingFilter(
        fields=(
            ('id', 'id'),
            ('-id', '-id'),
            ('brand', 'brand'),
            ('-brand', 'brand'),
        )
    )


class BrandModelFilter(filters.FilterSet):
    class Meta:
        model = BrandModelModel
        fields = {
            'id': ['lte', 'gte', 'exact'],
            'mark': ['startswith', 'endswith', 'contains'],
        }

    order = filters.OrderingFilter(
        fields=(
            ('id', 'id'),
            ('-id', '-id'),
            ('model', 'model'),
            ('-model', '-model'),
        )
    )
