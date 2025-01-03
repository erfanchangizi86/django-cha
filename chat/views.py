from django.shortcuts import render
from django.http import HttpRequest
import json 
from  django.utils.safestring import  mark_safe

# Create your views here.
def index(request):
    return render(request,'page/chat/index.html')


def RoomName(request:HttpRequest,room_name):
    user_name = request.user.username
    context = {
        'room_name': room_name,
        'user_name': mark_safe(json.dumps(user_name))
    }
    return render(request,'page/chat/room.html',context)
    