from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()

class Chat(models.Model):
    roomname = models.CharField(blank=True,max_length=200)
    members = models.ManyToManyField(user,null=True,blank=True)

    def __str__(self):
        return  self.roomname

class Message(models.Model):
    author = models.ForeignKey(user, verbose_name='نویسنده', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='متن')
    related_chat = models.ForeignKey(Chat,on_delete=models.CASCADE,blank=True,null=True)
    time = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')

    @classmethod
    def last_message(cls,room_name):
        return cls.objects.filter(related_chat__roomname = room_name).order_by('time')

    def __str__(self):
        return self.author.username
