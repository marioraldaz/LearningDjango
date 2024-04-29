from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from utils.validators import validate_positive_float, validate_activity_level
from .user_profile import UserProfile

class UserFitnessProfile(models.Model):
    GOAL_CHOICES = (
        ('Lose', 'Lose Weight'),
        ('Maintain', 'Maintain Weight'),
        ('Gain', 'Gain Weight')
    )

    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='fitness_profile')
    goal = models.CharField(max_length=10, choices=GOAL_CHOICES, default='Maintain')
    daily_calorie_intake_goal = models.PositiveIntegerField(default=2000, validators=[MinValueValidator(1200), MaxValueValidator(4500)])
    daily_protein_goal = models.FloatField(default=50.0, validators=[MinValueValidator(0), MaxValueValidator(500), validate_positive_float])
    daily_fat_goal = models.FloatField(default=70.0, validators=[MinValueValidator(0), MaxValueValidator(500), validate_positive_float])
    daily_carbohydrate_goal = models.FloatField(default=250.0, validators=[MinValueValidator(0), MaxValueValidator(1000), validate_positive_float])
    activity_level = models.PositiveIntegerField(default=1, validators=[validate_activity_level])

    def calculate_and_set_daily_calorie_intake_goal(self):
        # Calculate and set daily calorie intake goal based on user profile, activity level, and goal
        user_profile = self.user_profile
        age = timezone.now().date().year - user_profile.date_of_birth.year
        if user_profile.gender == 'Male':
            bmr = 88.362 + (13.397 * user_profile.weight) + (4.799 * user_profile.height) - (5.677 * age)
        else:
            bmr = 447.593 + (9.247 * user_profile.weight) + (3.098 * user_profile.height) - (4.330 * age)
        
        activity_multiplier = {
            1: 1.2,  # Sedentary
            2: 1.375,  # Lightly active
            3: 1.55,  # Moderately active
            4: 1.725,  # Very active
            5: 1.9  # Super active
        }

        calories_needed = bmr * activity_multiplier[self.activity_level]

        if self.goal == 'Lose':
            calories_needed -= 500  # Aim to create a calorie deficit of 500 calories per day for weight loss
        elif self.goal == 'Gain':
            calories_needed += 500  # Aim to create a calorie surplus of 500 calories per day for weight gain

        self.daily_calorie_intake_goal = int(calories_needed)
        self.save()

    def calculate_and_set_daily_protein_goal(self):
        # Calculate and set daily protein goal based on user profile and activity level
        # Protein goal formula: 1.0 gram of protein per pound of body weight
        self.daily_protein_goal = self.user_profile.weight * 1.0
        self.save()

    def calculate_and_set_daily_fat_goal(self):
        # Calculate and set daily fat goal based on user profile and activity level
        # Fat goal formula: 30% of total daily calories from fat (1 gram of fat = 9 calories)
        fat_calories = 0.30 * self.daily_calorie_intake_goal
        self.daily_fat_goal = fat_calories / 9.0  # Convert calories to grams
        self.save()

    def calculate_and_set_daily_carbohydrate_goal(self):
        # Calculate and set daily carbohydrate goal based on user profile and activity level
        # Carbohydrate goal formula: 50% of total daily calories from carbohydrates (1 gram of carbohydrate = 4 calories)
        carb_calories = 0.50 * self.daily_calorie_intake_goal
        self.daily_carbohydrate_goal = carb_calories / 4.0  # Convert calories to grams
        self.save()

    def __str__(self):
        return f"{self.user_profile.username}'s Fitness Profile"