# models/allergy.py
from django.db import models
from django.contrib.auth.models import User

class Allergies(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    # Add more fields as needed
    
    def __str__(self):
        return self.name
