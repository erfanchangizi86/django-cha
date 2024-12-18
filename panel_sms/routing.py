from django.urls import path
from .consumers import MyConsumer
websocket_urlpatterns = [
    path('ws/',MyConsumer),  # Replace with your consumer class name
]