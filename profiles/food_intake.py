from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class FoodIntake(models.Model):
    MEAL_CHOICES = [
        ('Breakfast', _('Breakfast')),
        ('Lunch', _('Lunch')),
        ('Dinner', _('Dinner')),
        ('Snack', _('Snack')),
    ]
   
    profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    meal_type = models.CharField(
        _('Meal Type'), max_length=20, choices=MEAL_CHOICES, default='Breakfast'
    )
    intake_date = models.DateField(_('Intake Date'), default=timezone.now)

    class Meta:
        db_table = 'profiles_foodintake' 
        
