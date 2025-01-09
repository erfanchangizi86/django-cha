from django.urls import path
from djangocha.settings import TEMPLATES
from .views  import index,RoomName
from django.contrib.auth import views

urlpatterns = [
    path('wsg/',index),
    path('<str:room_name>/',RoomName, name='room'),
    path('login',views.LoginView.as_view(template_name='page/chat/login.html'),name='login'),
    path('logout',views.LogoutView.as_view(template_name='page/chat/logged_out.html'), name='logout')
    ]

