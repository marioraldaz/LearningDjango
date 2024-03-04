# models/user_food_intake.py
from django.db import models
from django.contrib.auth.models import User
from .food import Food  # Import the Food model

class UserFoodIntake(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    date = models.DateField()
    serving_size = models.FloatField()
    number_of_servings = models.FloatField()
    # Add more fields as needed
    
    def __str__(self):
        return f"{self.user.username} - {self.food.name} - {self.date}"
    