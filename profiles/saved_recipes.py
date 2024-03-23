from django.db import models

class SavedRecipe(models.Model):
    recipe_id = models.IntegerField(unique=True, default=1)
    profile_id = models.IntegerField(default=1)

    def __str__(self):
        return f'Recipe {self.recipe_id} for Profile {self.profile_id}'