import django
from django.urls import path
from djangocha.settings import TEMPLATES
from .views  import index,RoomName,logout_view,formclass
from django.contrib.auth import views


urlpatterns = [
    path('wsg/',index.as_view(),name='index'),
    path('<str:room_name>/',RoomName, name='room'),
    path('login',views.LoginView.as_view(template_name='page/chat/login.html',),name='login'),
    path('logout', logout_view, name='logout'),
    path('register', formclass.as_view(), name='register'),


    ]

