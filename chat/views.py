from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponseForbidden
from django.urls import reverse_lazy
import json 
from  django.utils.safestring import  mark_safe
from django.contrib.auth.decorators import login_required
from chat.consumers import user
from .models import Chat
# Create your views here.
from django.contrib.auth import logout
from django.views.generic import FormView,ListView
from .forms import UserForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Max, Q

class index(LoginRequiredMixin, ListView):
    model = Chat
    template_name = 'page/chat/index.html'
    context_object_name = 'group'

    def get_queryset(self):
        """
        Override the get_queryset method to filter the chats based on the current user.
        """
        user = self.request.user
        queryset = super().get_queryset()
        queryset = queryset.filter(members=user)


        search = self.request.GET.get('search')
        
        if search is not None and search != "":
            print(search)
            queryset=queryset.filter(members=user,roomname__icontains=search)
        return queryset
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search')
        return context

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
    if user in chat_room.allowed_users.all():
        chat_room.members.add(user)
    else:
        return HttpResponseForbidden("<center><h1 style='background-color: #00f3ff;width: 50%;text-align: center;border-radius: 5px;'>شما مجوز پیوستن به این اتاق گفتگو را ندارید.</h1></center>")
        

# اگر دسترسی وجود دارد، اضافه کردن کاربر به اعضای اتاق
    

    user_name = request.user.username
    context = {
        'room_name': room_name,
        'user_name': mark_safe(json.dumps(user_name))
    }
    return render(request,'page/chat/room.html',context)


class formclass(FormView):
    form_class = UserForm
    template_name = 'page/chat/register.html'
    success_url = reverse_lazy('login')
    def form_valid(self, form):
        # ذخیره کاربر
        form.save()
        return super().form_valid(form)

def logout_view(request):
    logout(request)
    return redirect('login')



