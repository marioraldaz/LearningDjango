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
   
    profile = models.ForeignKey('UserProfile', default=1, on_delete=models.CASCADE)
    meal_type = models.CharField(
        _('Meal Type'), max_length=20, choices=MEAL_CHOICES, default='Breakfast'
    )
    intake_date = models.DateField(_('Intake Date'), default=timezone.now)
    def __str__(self):
        return f"{self.profile.username}'s {self.get_meal_type_display()} on {self.intake_date}"
