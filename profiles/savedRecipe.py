# models/saved_recipe.py
from django.db import models
from .user_recipe import UserRecipe
from django.contrib.auth.models import User

class SavedRecipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s saved recipe ({self.user_recipe or self.external_api_recipe})"
