from django.urls import path
from .views import HomeView
urlpatterns = [
    path("websocket",HomeView.as_view(),name='websocket')
]
