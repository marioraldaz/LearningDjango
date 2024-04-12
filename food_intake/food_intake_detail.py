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

    def __str__(self):
        return f"{self.food_item} for {self.food_intake}"
