from django.contrib.auth import get_user_model
from django_filters import rest_framework as filters


UserModel = get_user_model()


class UserFilter(filters.FilterSet):
    class Meta:
        model = UserModel
        fields = {
            'id': ['lte', 'gte', 'exact'],
            'email': ['startswith', 'endswith', 'contains'],

        }

    order = filters.OrderingFilter(
        fields=(
            ('id', 'id'),
            ('-id', '-id'),
            ('email', 'email'),
            ('-email', '-email'),
        )
    )
