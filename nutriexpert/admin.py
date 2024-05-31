from django.contrib import admin
from .models import NutriExpert

@admin.register(NutriExpert)
class ChatbotAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'created_at')


