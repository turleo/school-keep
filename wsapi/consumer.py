import json

from channels.auth import login
from channels.exceptions import DenyConnection
from channels.generic.websocket import AsyncWebsocketConsumer


class ApiConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        from django.contrib.auth.models import AnonymousUser
        message = json.loads(text_data)
        if self.scope["user"] == AnonymousUser() and message['event'].startswith('authentication'):
            token = callbacks[message['event']](self.scope, **message)
            if token is None:
                await self.close()
                return
            await login(self.scope, token.user)
            self.scope["session"].save()
            await self.send(json.dumps({"token": token.token}))
        elif self.scope["user"] == AnonymousUser():
            await self.close()
        else:
            await self.send(callbacks[message['event']](self.scope, **message))

    async def disconnect(self, code):
        pass


callbacks = {}
