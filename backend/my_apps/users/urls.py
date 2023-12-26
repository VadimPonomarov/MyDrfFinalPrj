from django.urls import path, include
from .views import UserCreateView, UserListView, UserActivateView, UserIsStaffToggleView, \
    ManageUserAccountsCRUDView, UserAccountCRUDView, UserAccountTypeToggleView, UserRUDView

urlpatterns = [
    path('', UserListView.as_view(), name='users_list'),
    path('/user/<int:pk>', UserRUDView.as_view(), name='users_user_RUD'),
    path('/create', UserCreateView.as_view(), name='users_create'),
    path('/activate/<str:token>', UserActivateView.as_view(), name='users_activate'),
    path('/<int:pk>/staff', UserIsStaffToggleView.as_view(), name='users_staff_toggle'),
    path('/account', UserAccountCRUDView.as_view(), name='users_user_account_CRUD'),
    path('/<int:pk>/account', ManageUserAccountsCRUDView.as_view(), name='users_manage_accounts_CRUD'),
    path('/<int:pk>/account/type_toggle', UserAccountTypeToggleView.as_view(), name='users_account_type_toggle'),
]
