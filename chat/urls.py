from django.urls import path
from . import views

urlpatterns = [
    path('wsg',views.index)
]
