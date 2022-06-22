
from channels.generic.websocket import AsyncWebsocketConsumer
import json


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("websocket connected")
        print("channel layer.........",self.channel_layer)  #get default channel layer from a project.
        print("channel name.........",self.channel_name) 

        self.user = self.scope["user"]
        print('userrrrrrrrrrrrrrrrrrrrrrr')
        print(self.user)
        print('userrrrrrrrrrrrrrrrrrrrrrr')

        # self.group_name=self.scope['url_route']['kwargs']  # get a group name
        # print(self.group_name) # get a group name
        
        self.group_name = "{}".format(self.user)
        print(self.group_name)

        # Join room group

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
           self.group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data=None,bytes_data = None):
        print("Message received from cleint...",text_data)

        await self.send(text_data='message from server to client')

    #     text_data_json = json.loads(text_data)
    #     message = text_data_json['msg']
    #     # Send message to room group
    #     await self.channel_layer.group_send(
    #         self.group_name,
    #         {
    #             'type': 'recieve_group_message',
    #             # "username": self.scope["user"].username,
    #             'message': message
    #         }
    #     )

    # async def recieve_group_message(self, event):
    #     message = event['message']

    #     # Send message to WebSocket
    #     await self.send(
    #          text_data=json.dumps({
    #         # "username": event["username"],
    #         'message': message
    #     }))