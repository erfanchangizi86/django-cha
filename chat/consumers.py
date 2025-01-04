import os
import django

# این خط را در ابتدای فایل قرار دهید تا Django بتواند اپلیکیشن‌ها را بارگذاری کند.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangocha.settings')
django.setup()  # این خط به Django اجازه می‌دهد که اپلیکیشن‌ها را بارگذاری کند.
from rest_framework.response import Response 
from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync
from chat.serializers import MessageSerializers
from chat.models import Message
from rest_framework.renderers import JSONRenderer

from django.contrib.auth import get_user_model

user = get_user_model()


class ChatConsumer(WebsocketConsumer):

    def new_message(self, data):
        message = data['message']
        username = data['username']
        us = user.objects.filter(username=username).first()
        mess:Message = Message.objects.create(author=us,text=message)
        result = self.message_serializer([mess])
        result = eval(result)
        self.send_to_message(result)
    
    def fetch_message(self, data):
        qs = Message.last_message()
        message_json = self.message_serializer(qs)
        content = {
            'message': eval(message_json)  # توجه داشته باشید که استفاده از eval خطرناک است.
        }
        self.chat_message(content)

    def message_serializer(self, qs):
        serializersd = MessageSerializers(qs, many=(lambda qs:True if (qs.__class__.__name__ == 'QuerySet') else False))
        content = JSONRenderer().render(serializersd.data)
        return content

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    commands = {
        'new_message': new_message,
        'fetch_message': fetch_message,
    }

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        command = text_data_json.get('command')
        data = text_data_json  # کل پیام را به متدهای مربوطه ارسال کنید.

        if command in self.commands:
            self.commands[command](self, data)  # 'self' و 'data' را به متد ارسال کنید.
        else:
            print(f"Unknown command: {command}")

    def send_to_message(self, message):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    def chat_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps({
            'message': message
                            }))