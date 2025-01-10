from django.shortcuts import render,redirect
from django.http import HttpRequest
import json 
from  django.utils.safestring import  mark_safe
from django.contrib.auth.decorators import login_required
from chat.consumers import user
from .models import Chat
# Create your views here.
from django.contrib.auth import logout

@login_required(login_url='login')
def index(request):
    user = request.user
    group_list = Chat.objects.filter(members=user)
    content = {
        'group':group_list
    }
    return render(request,'page/chat/index.html',content)

@login_required(login_url='login')
def RoomName(request:HttpRequest,room_name):
    user = request.user
    try:
        # تلاش برای پیدا کردن اتاق چت
        chat_room = Chat.objects.get(roomname=room_name)
    except Chat.DoesNotExist:
        # اگر اتاق پیدا نشد، ایجاد آن
        chat_room = Chat.objects.create(roomname=room_name)

    # اضافه کردن کاربر به اعضای اتاق
    chat_room.members.add(user)

    user_name = request.user.username
    context = {
        'room_name': room_name,
        'user_name': mark_safe(json.dumps(user_name))
    }
    return render(request,'page/chat/room.html',context)




def logout_view(request):
    logout(request)
    return redirect('login')



