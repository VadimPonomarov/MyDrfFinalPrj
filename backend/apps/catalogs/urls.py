from django.urls import path, include
from .views import SeedView, BrandListCreateView, BrandRetrieveUpdateDestroyView, BrandModelAddModelView, \
    BrandModelListView

urlpatterns = [
    path('/brands', BrandListCreateView.as_view(), name='catalogs_brand_list_create'),
    path('/brands/<int:pk>', BrandRetrieveUpdateDestroyView.as_view(), name='catalogs_brand_RUD'),
    path('/brands/<int:pk>/models', BrandModelAddModelView.as_view(), name='catalogs_models_list_create'),
    path('/models', BrandModelListView.as_view(), name='catalogs_models_list'),
    path('/localities/seed', SeedView.as_view(), name='catalogs_localities_seed'),
    # path('/brand/<int:pk>/model', BrandAddModelView.as_view(), name='catalogs_brand_model_create'),
    # path('/brand/<int:pk>/model/<int:model_pk>', CarBrandModelRetrieveUpdateDestroyView.as_view(),
    #      name='catalogs_model_RUD'),
]
