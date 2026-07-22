import json
from core.models import Notification
from channels.generic.websocket import AsyncWebsocketConsumer

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user=self.scope["user"]
        if self.user.is_authenticated: 
            self.group_name=f"user_{self.user.id}"
            await self.channel_layer.group_add(self.group_name, self.channel_name)
            print(f"{self.user.username} joined {self.group_name}")
            await self.accept()
        else:
            await self.close()
                
    async def receive(self, text_data):
        data=json.loads(text_data)
        message=data.get("message")
        await Notification.objects.acreate(reciever=self.user, title=data.get("title"), message=message)
        await self.send(text_data=json.dumps({'message':message}))

    async def notification_message(self, event):
        await self.send(text_data=json.dumps({
            "title": event["title"],
            "message": event["message"]
        }))

    async def disconnect(self, close_code):
        if hasattr(self, "group_name"):
            await self.channel_layer.group_discard(self.group_name, self.channel_name)
            print(f"{self.user.username} left {self.group_name}")
            print(f"disconnected with code: {close_code}")
        
        