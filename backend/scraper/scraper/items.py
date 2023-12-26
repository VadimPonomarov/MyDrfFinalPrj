from typing import Type

from scrapy_djangoitem import DjangoItem

from my_apps.catalogs.models import CarBrandModel, CarBrandModelModel


class CarBrandItem(DjangoItem):
    model = CarBrandModelModel
    fields = ['brand', 'model_name']
