from django.db import models
from profiles.user_profile import UserProfile
from django.core.validators import MinValueValidator
from profiles.utils.validators import validate_positive_float


class UserDaily(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    date = models.DateField()
    total_calories_consumed = models.FloatField(
        validators=[validate_positive_float, MinValueValidator(0)],default=0.0
        )
    total_protein_consumed = models.FloatField(
        validators=[validate_positive_float, MinValueValidator(0)],default=0.0
        )
    total_fat_consumed = models.FloatField(
        validators=[validate_positive_float, MinValueValidator(0)],default=0.0
        )
    total_carbohydrates_consumed = models.FloatField(
        validators=[validate_positive_float, MinValueValidator(0)],default=0.0
        )

    def __str__(self):
        return f"{self.profile.username} - {self.date}"
