from django.db import models
from profiles.user_profile import UserProfile
from utils.validators import validate_meal_type, validate_is_date_before_today

class FoodIntake(models.Model):
    MEAL_CHOICES = [
        ('Breakfast', ('Breakfast')),
        ('Lunch', ('Lunch')),
        ('Dinner', ('Dinner')),
        ('Snack', ('Snack')),
    ]
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE) 
    meal_type = models.CharField(
        validators=[validate_meal_type],
        max_length=20,
        choices=MEAL_CHOICES,
        blank = False
    )
    date = models.DateField(validators=[validate_is_date_before_today])

    class Meta:
        db_table = 'foodintake_foodintake'