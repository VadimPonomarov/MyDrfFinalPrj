import os

from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from configs.routing import websocket_urlpatterns
from core.middlewares.auth_socket_middleware import AuthSocketMiddleware

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configs.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AllowedHostsOriginValidator(
        AuthSocketMiddleware(
            URLRouter(websocket_urlpatterns)
        )
    )
})
