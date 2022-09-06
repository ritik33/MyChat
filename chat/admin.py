from django.contrib import admin
from .models import ChatRoom, Message


class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'user1', 'user2', 'room_name', 'timestamp']
    search_fields = ['id', 'room_name', 'user1__username',
                     'user2__username', 'user1__email', 'user2__email', ]
    readonly_fields = ['id', 'user1', 'user2', 'room_name', 'timestamp']

    class Meta:
        model = ChatRoom


class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'chat_room',  'from_user',
                    'to_user', 'content', 'timestamp']
    list_filter = ['chat_room',  'from_user', 'to_user', 'timestamp']
    search_fields = ['user__username', 'content']
    readonly_fields = ['id', 'content', 'from_user',
                       'to_user', 'chat_room', 'timestamp']

    class Meta:
        model = Message


admin.site.register(ChatRoom, ChatRoomAdmin)
admin.site.register(Message, MessageAdmin)
