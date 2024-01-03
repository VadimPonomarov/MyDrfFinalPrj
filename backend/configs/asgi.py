import os

from channels.routing import ProtocolTypeRouter, URLRouter
from configs.routing import websocket_urlpatterns
from core.middlewares.auth_socket_middleware import AuthSocketMiddleware

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configs.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthSocketMiddleware(URLRouter(websocket_urlpatterns))
})
