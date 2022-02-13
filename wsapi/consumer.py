import json

from channels.exceptions import DenyConnection
from channels.generic.websocket import AsyncWebsocketConsumer


class ApiConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        pass  # TODO: auth

    async def receive(self, text_data=None, bytes_data=None):
        message = json.loads(text_data)
        callbacks[message["event"]]()

    async def disconnect(self, code):
        pass


callbacks = {}
