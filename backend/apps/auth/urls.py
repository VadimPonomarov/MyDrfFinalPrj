from django.urls import include, path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import SocketView

urlpatterns = [
    path('/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('/socket', SocketView.as_view(), name='auth_socket_token')
]
