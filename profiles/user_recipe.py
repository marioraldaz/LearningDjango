from django.db import models
from django.contrib.auth.models import User

class UserRecipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    ingredients = models.TextField()
    instructions = models.TextField()
    # Add more fields as needed
    
    def __str__(self):
        return self.title

