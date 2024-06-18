from datetime import date
from django.conf import settings
from django.db import models


class Chat(models.Model):
  createdAt = models.DateField(default=date.today)


class Message(models.Model):
  text = models.CharField(max_length=500)
  createdAt = models.DateField(default=date.today)
  chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='chat_message_set', default=None, blank=True, null=True)
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author_message_set')
  reciever = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reciever_message_set')
  
  