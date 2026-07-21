import json
from core.models import Notification
from channels.generic.websocket import AsyncWebsocketConsumer

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("connected")
        await self.accept()

    async def receive(self, text_data):
        data=json.loads(text_data)
        message=data.get("message")
        await self.send(json.dumps({'message':message}))

    async def disconnect(self, close_code):
        print(f"channel dissconnect code - {close_code}")
        
        