from app import consumers
from django.urls import path
# from django.conf.urls import url,path

websocket_urlpatterns = [
    path('ws/', consumers.ChatConsumer.as_asgi()),
]




