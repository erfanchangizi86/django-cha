import json

from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        print(f"New connection: {self.scope['url_route']['kwargs']}")
        self.accept()

    def disconnect(self, close_code):
        print(f"Disconnected: {close_code}")

    def receive(self, text_data):
        print(f"Received: {text_data}")
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        self.send(text_data=json.dumps({"message": message}))

        