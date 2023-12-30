from django.urls import path, include
from .views import UserListCreateView, UserRetrieveUpdateDestroyView, UserActivateView, \
    ManageUserAccountsCRUDView, UserAccountCRUDView, UserAccountTypeToggleView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='users__list_create'),
    path('/user/<int:pk>', UserRetrieveUpdateDestroyView.as_view(), name='users__user_RUD'),
    path('/activate/<str:token>', UserActivateView.as_view(), name='users_activate'),
    path('/account', UserAccountCRUDView.as_view(), name='users_user_account_CRUD'),
    path('/<int:pk>/account', ManageUserAccountsCRUDView.as_view(), name='users_manage_accounts_CRUD'),
    path('/<int:pk>/account/type_toggle', UserAccountTypeToggleView.as_view(), name='users_account_type_toggle'),
]
