from django.urls import path, include

from my_apps.adds.views import AddsListCreateView, RetrieveUpdateDestroyView

urlpatterns = [
    path('', AddsListCreateView.as_view(), name='adds_list_create'),
    path('/<int:pk>', RetrieveUpdateDestroyView.as_view(), name='adds_RUD'),
]
