from django.db import models
from django.core.validators import MinLengthValidator
from django.core.validators import EmailValidator

from foods.recipe import Recipe
from utils.validators import validate_is_date_before_today,validate_positive_float, validate_activity_level
class UserProfile(models.Model):
    username = models.CharField(max_length=25, unique=True, validators=[MinLengthValidator(6)])
    password = models.CharField(max_length=85, validators=[MinLengthValidator(6)])
    gender = models.CharField(max_length=50,choices=(('Male', 'Male'), ('Female', 'Female')))
    email = models.EmailField(max_length=50, unique=True, validators=[EmailValidator(message="Enter a valid email address.")])
    weight = models.FloatField(default=80, validators=[validate_positive_float])
    height = models.FloatField(default=170, validators=[validate_positive_float])
    date_of_birth = models.DateField(validators=[validate_is_date_before_today])
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    activityLevel = models.PositiveIntegerField(default=1, validators=[validate_activity_level])
    saved_recipes = models.ManyToManyField(Recipe, related_name='saved_by_profiles', blank=True)

    def save_recipe(self, recipe):
        # Method to save a recipe for this user profile
        self.saved_recipes.add(recipe)

    def remove_recipe(self, recipe):
        # Method to remove a recipe from this user profile's saved recipes
        self.saved_recipes.remove(recipe)

    def get_saved_recipes(self):
        # Method to get all saved recipes for this user profile
        return self.saved_recipes.all()
    def __str__(self):
        return self.username