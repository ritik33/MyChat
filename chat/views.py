from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.db.models import Q
from django.views import View

from account.serializers import UserSerializer
from .serializers import MessageSerializer
from .models import ChatRoom, Message
from django.contrib.auth import get_user_model

User = get_user_model()


class ChatRoomView(View):
    template_name = 'chat/chatroom.html'

    def get_chats(self, me, friend):
        chat_room = None
        try:
            chat_room = ChatRoom.objects.get(
                (Q(user1=me) & Q(user2=friend)) | (Q(user1=friend) & Q(user2=me)))
            return Message.objects.order_by('-timestamp').filter(chat_room=chat_room)
        except:
            return None

    def get(self, request, friend):
        user = request.user
        context = {}
        if user.is_authenticated:
            user_serialized_data = UserSerializer(user)
            friend = User.objects.get(username=friend)
            friend_serialized_data = UserSerializer(friend)

            all_chats = self.get_chats(user, friend)
            if all_chats is not None:
                chat_serialized_data = MessageSerializer(all_chats, many=True)
                context = {
                    'me': user_serialized_data.data,
                    'friend': friend_serialized_data.data,
                    'chats': chat_serialized_data.data
                }
            else:
                context = {
                    'me': user_serialized_data.data,
                    'friend': friend_serialized_data.data,
                    'chats': ''
                }

            return render(request, self.template_name, context)
        return redirect('login')
