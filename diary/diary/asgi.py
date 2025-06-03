"""
ASGI config for diary project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

from notifications import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'diary.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    ),
})

# or if you have other routing files you can do this
# application = ProtocolTypeRouter({
#     'http': get_asgi_application(),
#     'websocket': AuthMiddlewareStack(
#         URLRouter([
#             *routing.websocket_urlpatterns,
#             *other_routing1.websocket_urlpatterns,
#             *other_routing2.websocket_urlpatterns,
#         ])
#     ),
# })