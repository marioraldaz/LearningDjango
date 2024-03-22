from django.db import models

class SavedRecipe(models.Model):
    profile_id = models.IntegerField()
    recipe_id = models.IntegerField(unique=True)

    def __str__(self):
        return f'Recipe {self.recipe_id} for Profile {self.profile_id}'