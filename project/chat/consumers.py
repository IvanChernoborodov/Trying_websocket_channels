from channels.generic.websocket import AsyncWebsocketConsumer
import json

class EchoConsumer(AsyncWebsocketConsumer):
    # groups = ["broadcast"]

    async def connect(self):
        # Called on connection.
        # To accept the connection call:
        await self.accept()

        # Or accept the connection and specify a chosen subprotocol.
        # A list of subprotocols specified by the connecting client
        # will be available in self.scope['subprotocols']
        # await self.accept("subprotocol")
        # To reject the connection, call:
        # await self.close()

    async def receive(self, text_data=None, bytes_data=None):
        # Called with either text_data or bytes_data for each frame
        # You can call:
        await self.send(text_data="Hello world!")

        # Or, to send a binary frame:
        # await self.send(bytes_data="Hello world!")

        # Want to force-close the connection? Call:
        # await self.close()
        # Or add a custom WebSocket error code!
        # await self.close(code=4123)

    async def disconnect(self, close_code):
        print('closed')
        # Called when the socket closes
        await self.close()









# def it():
#     i = 0
#     while True:
#         yield i
#         i += 1
#
# x = it()
# async def prod():
#     async for i in x:
#         return i


# class ChatConsumer(AsyncWebsocketConsumer):
    # async def connect(self):
    #     # print(dir(self.scope))
    #     # self.room_name = self.scope['url_route']['kwargs']['room_name']
    #     # print(self.room_name)
    #     # self.room_group_name = 'chat_%s' % self.room_name
    #     # Join room group
    #     # await self.channel_layer.group_add(
    #     #     self.room_group_name,
    #     #     self.channel_name
    #     # )
    #     print('connected')
    #     await self.accept()

    # async def disconnect(self, close_code):
    #     # Leave room group
    #     print('disconected')
    #     await self.channel_layer.group_discard(
    #         self.room_group_name,
    #         self.channel_name
    #     )

    # Receive message from WebSocket
    # async def receive(self, text_data):
    #     text_data_json = json.loads(text_data)
    #     message = text_data_json['message']
    #
    #     # Send message to room group
    #     await self.channel_layer.group_send(
    #         self.room_group_name,
    #         {
    #             'type': 'chat_message',
    #             'message': message
    #         }
    #     )

    # Receive message from room group
    # async def chat_message(self, event):
    #     message = event['message']
    #     print(message)
    #     # Send message to WebSocket
    #     await self.send(text_data=json.dumps({
    #         'message': message,
    #     }))