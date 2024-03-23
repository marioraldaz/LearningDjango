from django.db import models

class UserRecipe(models.Model):
    recipe_id = models.IntegerField(unique=True, default=1)
    profile_id = models.IntegerField(default=1)
    title = models.CharField(max_length=100)
    ingredients = models.TextField()
    instructions = models.TextField()
    
    def __str__(self):
        return self.title

