from django.db import models
from .ingredient import Ingredient
from utils.validators import validate_positive_float
from django.core.validators import MinValueValidator
from django.contrib.postgres.fields import JSONField

class Recipe(models.Model):
    profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.URLField(max_length=600)
    servings = 2
    readyInMinutes = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0)] )
    instructions = models.TextField()
    ingredients = models.ManyToManyField(Ingredient, related_name='recipes')
    spoonacular_id = models.IntegerField(unique=True)
    sourceName = models.CharField(max_length=100)
    sourceUrl = models.URLField(max_length=600)
    healthScore = models.FloatField(null=True, validators=[validate_positive_float])
    spoonacularScore = models.FloatField(null=True, validators=[validate_positive_float])
    pricePerServing = models.FloatField(null=True, validators=[validate_positive_float])
    analyzedInstructions = JSONField(null=True)
    cheap = models.BooleanField(default=False, null=True)
    creditsText = models.TextField(null=True, max_length=200)
    cuisines = JSONField(null=True)
    dairyFree = models.BooleanField(default=False, null=True)
    diets = models.JSONField(null=True)
    gaps = models.CharField(max_length=10, null=True)
    glutenFree = models.BooleanField(null=True)
    instructions = models.TextField(null=True)
    ketogenic = models.BooleanField(null=True)
    lowFodmap = models.BooleanField(null=True)
    occasions = models.JSONField(null=True)
    sustainable = models.BooleanField(null=True)
    vegan = models.BooleanField(null=True)
    vegetarian = models.BooleanField(null=True)
    veryHealthy = models.BooleanField(null=True)
    veryPopular = models.BooleanField(null=True)
    whole30 = models.BooleanField(null=True)
    weightWatcherSmartPoints = models.IntegerField(null=True)
    dishTypes = models.JSONField(null=True)
    extendedIngredients = models.JSONField(null=True)
    summary = models.TextField(null=True)
    winePairing = models.JSONField(null=True)
    
    def add_ingredient(self, ingredient):
        self.ingredients.add(ingredient)

    def remove_ingredient(self, ingredient):
        self.ingredients.remove(ingredient)

    def get_ingredients(self):
        return self.ingredients.all()
    
    def __str__(self):
        return self.title

