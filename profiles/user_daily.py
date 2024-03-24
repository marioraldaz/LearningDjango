from django.db import models
from .user_profile import UserProfile

class DailyNutritionalStats(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    date = models.DateField()
    total_calories_consumed = models.FloatField(default=0.0)
    total_protein_consumed = models.FloatField(default=0.0)
    total_fat_consumed = models.FloatField(default=0.0)
    total_carbohydrates_consumed = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.profile.username} - {self.date}"
