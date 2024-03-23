from django.db import models
from .food_intake import FoodIntake

class FoodIntakeDetail(models.Model):
    id = models.AutoField(primary_key=True)
    food_intake = models.ForeignKey(FoodIntake, on_delete=models.CASCADE, related_name='details')
    item_name = models.CharField(max_length=255)
    item_type = models.CharField(max_length=20)  # 'Ingredient' or 'Recipe'

    def __str__(self):
        return f"{self.item_name} ({self.item_type}) for {self.food_intake}"