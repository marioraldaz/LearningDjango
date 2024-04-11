from django.db import models
from .food_intake import FoodIntake
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MinValueValidator
from foods.ingredient import Ingredient
from foods.recipe import Recipe

class FoodIntakeDetail(models.Model):
    food_intake = models.ForeignKey(FoodIntake, on_delete=models.CASCADE, related_name='details')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='food_intakes', null=True, blank=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='food_intakes', null=True, blank=True)

    # Ensure only one of the foreign keys is set using OneToOneField
    food_id = models.OneToOneField(Ingredient, on_delete=models.CASCADE, related_name='food_intake', null=True, blank=True)    amount = models.IntegerField(default=1, validators=[MinValueValidator(0)])
    def __str__(self):
        return f"{self.item_name} ({self.item_type}) for {self.food_intake}"
    
    