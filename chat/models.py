from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


User = get_user_model()


class ChatRoom(models.Model):
    user1 = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user1")
    user2 = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user2")
    timestamp = models.DateTimeField(default=timezone.now)

    @property
    def room_name(self):
        return f"ChatRoom-{self.id}"

    def __str__(self):
        return self.room_name

    class Meta:
        ordering = ['-timestamp']


class Message(models.Model):
    from_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='from_user')
    to_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='to_user')
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    def __str__(self):
        return self.id
