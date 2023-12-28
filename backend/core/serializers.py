from rest_framework.serializers import ModelSerializer

from core.models import BaseModel


class BaseSerializer(ModelSerializer):
    class Meta:
        model = BaseModel
        fields = '__all__'
