from django.db import models
from .nutrition import Nutrition
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    spoonacular_id = models.IntegerField(unique=True)
    original = models.CharField(max_length=255, null=True)
    originalName = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255, null=True)
    amount = models.FloatField(null=True)
    unit = models.CharField(max_length=50, null=True)
    unitShort = models.CharField(max_length=50, null=True)
    unitLong = models.CharField(max_length=50, null=True)
    possibleUnits = models.JSONField(null=True)
    estimatedCost_value = models.FloatField(null=True)
    estimatedCost_unit = models.CharField(max_length=50, null=True)
    consistency = models.CharField(max_length=50, null=True)
    shoppingListUnits = models.JSONField(null=True)
    aisle = models.CharField(max_length=255, null=True)
    image = models.URLField(null=True)
    meta = models.JSONField(null=True)
    nutrition = models.OneToOneField(Nutrition, on_delete=models.CASCADE, related_name='recipe')
    categoryPath = models.JSONField(null=True)

    @classmethod
    def add(cls, name, spoonacular_id):
        ingredient = cls.objects.create(name=name, spoonacular_id=spoonacular_id)
        return ingredient
    