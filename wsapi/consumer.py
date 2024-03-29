import json

from channels.auth import login, logout
from channels.generic.websocket import AsyncWebsocketConsumer


class ApiConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.user = None

    async def connect(self):
        await self.accept()
        await self.send(json.dumps({"event": "authentication.auth"}))

    async def receive(self, text_data=None, bytes_data=None):
        message = json.loads(text_data)
        if message['event'].startswith('authentication.'):
            token = callbacks[message['event']](self.scope, **message)
            if token is None:
                await self.send(json.dumps({"event": "authentication.error"}))
                return
            self.user = token.user
            token.last_ip = self.scope['client'][0]
            token.save()
            if token is None:
                await self.send(json.dumps({"event": "authentication.error"}))
            else:
                await self.send(json.dumps({"event": "authentication.token", "token": token.token}))
        elif self.user is None:
            await self.send(json.dumps({"event": "authentication.auth"}))
        elif message['event'] == 'authentication.logout':
            await logout(self.scope)
            await self.close()
        else:
            self.scope['user'] = self.user
            answer = callbacks.get(message['event'], lambda x, **kwargs: "Oops")(self.scope, **message)
            answer = json.dumps(answer)
            await self.send(answer)

    async def disconnect(self, code):
        pass


callbacks = {}
