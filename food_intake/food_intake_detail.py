from django.db import models
from .food_intake import FoodIntake
from django.contrib.contenttypes.models import ContentType


class FoodIntakeDetail(models.Model):
    food_intake = models.ForeignKey(FoodIntake, on_delete=models.CASCADE, related_name='details')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    food_id = models.CharField(max_length=255)
    amount = models.IntegerField(default=1)
    def __str__(self):
        return f"{self.item_name} ({self.item_type}) for {self.food_intake}"
    
    