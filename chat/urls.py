from django.urls import path
from . import views

urlpatterns = [
    path('wsg/',views.index),
    path('<str:room_name>/',views.RoomName, name='room'),
]

