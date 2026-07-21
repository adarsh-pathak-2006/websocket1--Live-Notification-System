from channels.generic.websocket import WebsocketConsumer
import json

class NotificationConsumer(WebsocketConsumer):
    async def connect(self):
        print("client connected")
        await self.accept()

        await self.send(text_data=json.dump({'message':'welcome to the webscoket'}))


    async def receive(self, text_data):
        data=json.loads(text_data)
        message=data.get("message")
        print(f"parsed data- {message}")

        await self.send(json.dumps({'message':message}))

    async def disconnect(self, code):
        print(f"connection terminated- {code}")
