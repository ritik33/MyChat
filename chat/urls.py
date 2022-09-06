from django.urls import path
from chat.views import (
    ChatRoomView
)

app_name = 'chat'

urlpatterns = [
    path('<str:friend>/', ChatRoomView.as_view(), name='chatroom'),
]
