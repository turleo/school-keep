"""
ASGI config for schoolSync project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

import django
from channels.auth import AuthMiddlewareStack
from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter, URLRouter

import wsapi.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'schoolSync.settings')

django.setup()

application = ProtocolTypeRouter({
  "http": AsgiHandler(),
  "websocket": AuthMiddlewareStack(
    URLRouter(
      wsapi.routing.websocket_urlpatterns
    )
  ),
})

