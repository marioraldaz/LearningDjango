from django.db import models
from .food_intake import FoodIntake


class FoodIntakeDetail(models.Model):
    id = models.AutoField(primary_key=True)
    food_intake = models.ForeignKey(FoodIntake, on_delete=models.CASCADE, related_name='details')
    food_id = models.CharField(max_length=255)
    amount = models.IntegerField(default=1)
    def __str__(self):
        return f"{self.item_name} ({self.item_type}) for {self.food_intake}"