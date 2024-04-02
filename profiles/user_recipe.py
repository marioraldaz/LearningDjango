from django.db import models

class UserRecipe(models.Model):
    profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    ingredients = models.TextField()
    instructions = models.TextField()
    
    def __str__(self):
        return self.title

