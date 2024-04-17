from django.db import models
from profiles.user_profile import UserProfile
from utils.validators import validate_meal_type, validate_is_date_before_today
from django.utils.translation import gettext_lazy as _
import datetime
class FoodIntake(models.Model): 
    MEAL_CHOICES = [
        ('Breakfast', _('Breakfast')),
        ('Lunch', _('Lunch')),
        ('Dinner', _('Dinner')),
        ('Snack', _('Snack')),
    ]
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True) 
    meal_type = models.CharField(
        validators=[validate_meal_type],
        max_length=20, choices=MEAL_CHOICES
    )
    date = models.DateField(default=datetime.date(2024, 1, 1),
        validators=[validate_meal_type])
    class Meta:
        db_table = 'profiles_foodintake' 
        
