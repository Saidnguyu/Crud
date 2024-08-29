from django.contrib import admin
from .models import ChatItem, ChatBot

# Register your models here.

admin.site.register(ChatBot)
admin.site.register(ChatItem)
