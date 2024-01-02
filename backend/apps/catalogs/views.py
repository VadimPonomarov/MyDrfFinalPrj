import json
import os

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response

import pandas as pd
from apps.catalogs.models import CarBrandModel, CarBrandModelModel
from apps.catalogs.serializers import CarBrandModelSerializer, CarBrandSerializer

from .models import LocalitiesModel
from .serializers import LocalitiesSerializer


class BrandListCreateView(ListCreateAPIView):
    queryset = CarBrandModel.objects.all()
    serializer_class = CarBrandSerializer
    permission_classes = [AllowAny]


class BrandRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarBrandModel.objects.all()
    serializer_class = CarBrandSerializer
    permission_classes = [IsAdminUser]


class BrandModelAddModelView(GenericAPIView):
    queryset = CarBrandModel.objects.all()
    serializer_class = CarBrandSerializer
    permission_classes = [IsAdminUser]

    def post(self, *args, **kwargs):
        get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
        serializer = CarBrandModelSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        model = CarBrandModelModel.objects.create(
            brand_id=self.kwargs["pk"],
            **serializer.validated_data
        )
        serializer = CarBrandModelSerializer(model)
        return Response(serializer.data, status.HTTP_200_OK)


class BrandModelListView(ListAPIView):
    queryset = CarBrandModelModel.objects.all().select_related('brand')
    serializer_class = CarBrandModelSerializer
    permission_classes = [AllowAny]


class SeedView(GenericAPIView):
    queryset = LocalitiesModel.objects.all()
    serializer_class = LocalitiesSerializer
    permission_classes = [AllowAny]

    def get(self, *args, **kwargs):
        is_seeded = LocalitiesModel.objects.all().count()
        if is_seeded:
            return HttpResponse("!!! Failure. Table is not empty yet", status.HTTP_400_BAD_REQUEST)
        data = pd.read_json(os.path.join(settings.BASE_DIR, "static/dict/ua_locations_10_11_2021_conv2.json"))
        df = pd.DataFrame(data)
        json_string = json.dumps(df.to_dict(orient="records"), indent=4, ensure_ascii=False)
        json_list = json.loads(json_string)

        for i in json_list:
            try:
                print(i)
                LocalitiesModel.objects.create(locale_id=i.get('id'), **i)
            except:
                pass

        return HttpResponse("!!! Success", status.HTTP_200_OK)
