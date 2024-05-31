from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models


class NutriExpert(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    #user = models.ForeignKey(Chatbot, on_delete=models.CASCADE)
    input_text = models.TextField()
    response_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User: {self.user.username}, Input: {self.input_text[:50]}, Response: {self.response_text[:50]}"