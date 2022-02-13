from django.urls import path

from .consumer import ApiConsumer

websocket_urlpatterns = [
    path('wsapi/', ApiConsumer.as_asgi()),
]
