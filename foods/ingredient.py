from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    spoonacular_id = models.IntegerField(unique=True)

    @classmethod
    def add(cls, name, spoonacular_id):
        ingredient = cls.objects.create(name=name, spoonacular_id=spoonacular_id)
        return ingredient
    