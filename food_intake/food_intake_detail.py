import json
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from foods.nutrition import Nutrition
from .food_intake import FoodIntake
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MinValueValidator
from foods.ingredient import Ingredient
from foods.recipe import Recipe
from django.core.serializers import serialize

class FoodIntakeDetail(models.Model):
    food_intake = models.ForeignKey(FoodIntake, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1, validators=[MinValueValidator(0)])


    def get_nutrients_data(self):
        nutrition = self.recipe.nutrition
        nutrition = serialize('json', [nutrition])
        nutrition = json.loads(nutrition)
        return nutrition[0]['fields']['nutrients']

    def get_properties_data(self):
        nutrition =self.recipe.nutrition
        nutrition = serialize('json', [nutrition])
        nutrition = json.loads(nutrition)
        return nutrition[0]['fields']['properties']


    def get_flavonoids_data(self):
        nutrition =self.recipe.nutrition
        nutrition = serialize('json', [nutrition])
        nutrition = json.loads(nutrition)
        return nutrition[0]['fields']['flavonoids']


    def get_caloric_breakdown_data(self):
        nutrition =self.recipe.nutrition
        caloric_breakdown_data = {}
        caloric_breakdown_data['percent_proteins'] = nutrition.percent_protein
        caloric_breakdown_data['percent_fat'] = nutrition.percent_fat
        caloric_breakdown_data['percent_carbs'] = nutrition.percent_carbs
        return caloric_breakdown_data

    def get_weight_per_serving_data(self):
        nutrition =self.recipe.nutrition
        weight_per_serving_data = nutrition.weight_per_serving
        return weight_per_serving_data
    def __str__(self):
        return f"{self.recipe.title} for {self.food_intake.meal_type}"
