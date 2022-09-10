from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model
from django.db.models import Q
from asgiref.sync import sync_to_async
import json
from account.serializers import UserSerializer
from .models import ChatRoom, Message


User = get_user_model()


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        user = self.scope['user']

        # get object of friend
        friend = await sync_to_async(User.objects.get)(username=self.scope['url_route']['kwargs']['friend'])

        # create a chatroom object if it doesn't exist
        chat_room = None
        try:
            chat_room = await sync_to_async(ChatRoom.objects.get)((Q(user1=user) & Q(user2=friend)) | (Q(user1=friend) & Q(user2=user)))
        except:
            chat_room = await sync_to_async(ChatRoom.objects.create)(user1=user, user2=friend)
        finally:
            self.room_name = chat_room.room_name

        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_name,
            self.channel_name
        )

    async def receive(self, text_data):
        payload = json.loads(text_data)
        from_user = await sync_to_async(User.objects.get)(username=payload['user']['username'])
        to_user = await sync_to_async(User.objects.get)(username=payload['friend']['username'])

        chat_room = await sync_to_async(ChatRoom.objects.get)((Q(user1=from_user) & Q(user2=to_user)) | (Q(user1=to_user) & Q(user2=from_user)))
        message = await sync_to_async(Message.objects.create)(content=payload['message'], from_user=from_user, to_user=to_user, chat_room=chat_room)

        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': 'chatroom.message',
                'user': message.from_user,
                "profile_image": self.scope["user"].profile_image,
                'message': message.content
            }
        )

    async def chatroom_message(self, event):
        serialized_data = UserSerializer(event['user'])
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'user': serialized_data.data
        }))
