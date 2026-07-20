from django.urls import path
from core.consumers import NotificationConsumer

websocket_urlpatterns=[
    path('ws/notification/', NotificationConsumer.as_asgi(), name='notification'),
]