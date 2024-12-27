from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.
def index(request):
    return render(request,'page/chat/index.html')


def RoomName(request:HttpRequest,room_name):
    print(request)
    context = {
        'room_name':room_name
    }
    return render(request,'page/chat/room.html',context)
    