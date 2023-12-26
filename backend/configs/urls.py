from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt

from rest_framework.permissions import AllowAny

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from graphene_django.views import GraphQLView
from my_apps.adds import urls as adds
from my_apps.auth import urls as auth
from my_apps.catalogs import urls as catalogs
from my_apps.users import urls as users

schema_view: get_schema_view = get_schema_view(
    openapi.Info(
        title='Titel',
        default_version='1.0.0',
        description="Description ..."
    ),
    public=True,
    permission_classes=[AllowAny],

)

urlpatterns = [
    path('api', include(auth)),
    path('api/users', include(users)),
    path('api/catalogs', include(catalogs)),
    path('api/adds', include(adds)),
    # path('api/silk', include('silk.urls', namespace='silk')),
    path('api/doc', schema_view.with_ui('swagger', cache_timeout=0)),
    path("api/graphql", GraphQLView.as_view(graphiql=True)),
    # path("api/graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
