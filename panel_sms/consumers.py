from channels.generic.websocket import WebSocketConsumer

class MyConsumer(WebSocketConsumer):
    def connect(self):
        self.accept()
    def disconnect(self,close_code):
        return
    def receive(self, text_data):
        self.send(text_data=text_data)