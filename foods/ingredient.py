from django.db import models
from .nutrition import Nutrition
class Ingredient(models.Model):
    nutrition = models.OneToOneField(Nutrition, on_delete=models.CASCADE, related_name='recipe_ingredient')
    spoonacular_id = models.IntegerField(unique=True, null=True, blank=True)
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
    categoryPath = models.JSONField(null=True)

    @classmethod
    def create_with_nutrition(cls, name, spoonacular_id, ingredient_data):
        # Create Nutrition object using Nutrition.create_from_json method
        nutrition = Nutrition.create_from_json(ingredient_data.get('nutrition'))

        # Create Ingredient object with the associated Nutrition
        ingredient = cls.objects.create(
            name=name,
            spoonacular_id=spoonacular_id,
            nutrition=nutrition,
            original=ingredient_data.get('original'),
            originalName=ingredient_data.get('originalName'),
            amount=ingredient_data.get('amount'),
            unit=ingredient_data.get('unit'),
            unitShort=ingredient_data.get('unitShort'),
            unitLong=ingredient_data.get('unitLong'),
            possibleUnits=ingredient_data.get('possibleUnits'),
            estimatedCost_value=ingredient_data.get('estimatedCost', {}).get('value'),
            estimatedCost_unit=ingredient_data.get('estimatedCost', {}).get('unit'),
            consistency=ingredient_data.get('consistency'),
            shoppingListUnits=ingredient_data.get('shoppingListUnits'),
            aisle=ingredient_data.get('aisle'),
            image=ingredient_data.get('image'),
            meta=ingredient_data.get('meta'),
            categoryPath=ingredient_data.get('categoryPath')
        )

        return ingredient