from channels.generic.websocket import AsyncWebsocketConsumer
import json
import time
import asyncio
import random


async def gener():
    while True:
        yield str(random.random())
x = gener()
async def producer():
    async for i in x:
        await asyncio.sleep(2)
        return str(i)


class EchoConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        # Called on connection.
        # To accept the connection call:
        await self.accept()
        while True:
            await self.send(text_data= await producer())

        # Or accept the connection and specify a chosen subprotocol.
        # A list of subprotocols specified by the connecting client
        # will be available in self.scope['subprotocols']
        # await self.accept("subprotocol")
        # To reject the connection, call:
        # await self.close()


    # async def disconnect(self, close_code):
    #     print('closed')
    #     # Called when the socket closes
    #     await self.close()

    # async def receive(self, text_data=None, bytes_data=None):


        # Called with either text_data or bytes_data for each frame
        # You can call:
        # await self.send(text_data="Hello world!")
        # await self.send(text_data=await producer())

        # Or, to send a binary frame:
        # await self.send(bytes_data="Hello world!")

        # Want to force-close the connection? Call:
        # await self.close()
        # Or add a custom WebSocket error code!
        # await self.close(code=4123)




class FuckingConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # for k,v in self.scope.items():
        #     print(k)
        self.room_name = 'test'
        self.room_group_name = 'freaks'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        print(self.room_name)
        print(self.room_group_name)
        print(self.channel_name)
        # Send message to room group

        await self.accept()
        # await self.send(text_data=await producer())

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': 'hello',
            }
        )



    async def disconnect(self, close_code):
        print('left')
        await self.channel_layer.group_discard(
            'test_room',
            self.channel_name
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))

