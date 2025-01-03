from rest_framework import serializers
from .models import Message

class MessageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['__str__', 'text', 'time']
