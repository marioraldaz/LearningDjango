from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from .food_intake import FoodIntake
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MinValueValidator
from foods.ingredient import Ingredient
from foods.recipe import Recipe

class FoodIntakeDetail(models.Model):
    food_intake = models.ForeignKey(FoodIntake, on_delete=models.CASCADE, related_name='details')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    food_id = models.PositiveIntegerField()
    food_item = GenericForeignKey('content_type', 'food_id')
    amount = models.IntegerField(default=1, validators=[MinValueValidator(0)])



    def get_nutrients_data(self):
        nutrients_data = {}
        for nutrient in self.nutrition.get('nutrients', []):
            name = nutrient['name']
            amount = nutrient['amount']
            nutrients_data[name] = amount
        return nutrients_data

    def get_properties_data(self):
        properties_data = {}
        for prop in self.nutrition.get('properties', []):
            name = prop['name']
            amount = prop['amount']
            properties_data[name] = amount
        return properties_data

    def get_flavonoids_data(self):
        flavonoids_data = {}
        for flavonoid in self.nutrition.get('flavonoids', []):
            name = flavonoid['name']
            amount = flavonoid['amount']
            flavonoids_data[name] = amount
        return flavonoids_data

    def get_caloric_breakdown_data(self):
        caloric_breakdown_data = self.nutrition.get('caloricBreakdown', {})
        return caloric_breakdown_data

    def get_weight_per_serving_data(self):
        weight_per_serving_data = self.nutrition.get('weightPerServing', {})
        return weight_per_serving_data
    def __str__(self):
        return f"{self.food_item} for {self.food_intake}"
