from django.contrib import admin
from .models import Chatbot

@admin.register(Chatbot)
class ChatbotAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'created_at')


