from django.urls import path
from . import consumers
websocket_urlpatterns = [
    path('ws/', consumers.MyConsumer),  # Replace with your consumer class name
]