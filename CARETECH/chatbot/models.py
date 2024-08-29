from django.db import models
from account.models import Account


# Create your models here.

class ChatItem(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    message = models.TextField(max_length=1000)
    response = models.TextField(max_length=2000)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Chat Item"
        verbose_name_plural = 'Chat Items'


class ChatBot(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_created=True)
    chat_items = models.ForeignKey(ChatItem, on_delete=models.CASCADE)
