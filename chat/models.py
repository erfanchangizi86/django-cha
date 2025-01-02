from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
user = get_user_model()

class Message(models.Model):
    author = models.ForeignKey(user,verbose_name='نویسنده',on_delete=models.CASCADE)
    text = models.TextField(verbose_name='متن')
    time = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ')
    
    def last_message(self):
        return Message.objects.all().order_by('-time')
    
    def __str__(self):
        return self.author.username
    