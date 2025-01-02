import os
import django

# این خط را در ابتدای فایل قرار دهید تا Django بتواند اپلیکیشن‌ها را بارگذاری کند.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangocha.settings')
django.setup()  # این خط به Django اجازه می‌دهد که اپلیکیشن‌ها را بارگذاری کند.

from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync
from chat.serializers import MessageSerializers
from chat.models import Message
from rest_framework.renderers import JSONRenderer
class ChatConsumer(WebsocketConsumer):

    def new_message(self,data):
        print('hello')

    def fetch_message(self,data):
        qs = Message.last_message(self)
        message_json = self.message_serializer(qs)
        content =  {
            'message':eval(message_json)
        }
        self.chat_message(content)

    def message_serializer(self,qs):
        serializersd = MessageSerializers(qs,many=True)
        conect = JSONRenderer().render(serializersd.data)
        return conect
    
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
    commands = {
        'new_message':new_message,
        'fetch_message': fetch_message,
    }
    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json.get('message',None)
        command = text_data_json['command']

        self.commands[command](message)
    
    def send_to_message(self,message):
        
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    def chat_message(self, event):
        message = event['message']
        print(event)
        self.send(text_data=json.dumps({
            'message': "You: "+message
        }))
