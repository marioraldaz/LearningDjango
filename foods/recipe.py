from django.db import models
from .ingredient import Ingredient
from utils.validators import validate_positive_float
from django.core.validators import MinValueValidator
from .nutrition import Nutrition
from django.db import transaction
import requests

class Recipe(models.Model):
    id = models.IntegerField(primary_key=True)
    nutrition = models.OneToOneField(Nutrition, on_delete=models.CASCADE, related_name='recipe_nutrition')
    ingredients = models.ManyToManyField(Ingredient, related_name='recipes')
    title = models.CharField(max_length=100)
    image = models.URLField(max_length=600)
    servings = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0)] )
    readyInMinutes = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0)] )
    instructions = models.TextField()
    spoonacular_id = models.IntegerField(unique=True, null=True, blank=True)
    sourceName = models.CharField(max_length=100)
    sourceUrl = models.URLField(max_length=600)
    healthScore = models.FloatField(null=True, validators=[validate_positive_float])
    spoonacularScore = models.FloatField(null=True, validators=[validate_positive_float])
    pricePerServing = models.FloatField(null=True, validators=[validate_positive_float])
    analyzedInstructions = models.JSONField(null=True)
    cheap = models.BooleanField(default=False, null=True)
    creditsText = models.TextField(null=True, max_length=200)
    cuisines = models.JSONField(null=True)
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
    
    
    @classmethod
    def create_with_nutrition(cls, recipe_data):
        nutrition_data = recipe_data.get('nutrition')

        # Create Nutrition object using Nutrition.create_from_json method
        nutrition = Nutrition.create_from_json(nutrition_data)

        # Create Recipe object with the associated Nutrition
        recipe = cls.objects.create(
            nutrition=nutrition,
            title=recipe_data.get('title'),
            image=recipe_data.get('image'),
            servings=recipe_data.get('servings'),
            readyInMinutes=recipe_data.get('readyInMinutes'),
            instructions=recipe_data.get('instructions'),
            spoonacular_id=recipe_data.get('spoonacular_id'),
            sourceName=recipe_data.get('sourceName'),
            sourceUrl=recipe_data.get('sourceUrl'),
            healthScore=recipe_data.get('healthScore'),
            spoonacularScore=recipe_data.get('spoonacularScore'),
            pricePerServing=recipe_data.get('pricePerServing'),
            analyzedInstructions=recipe_data.get('analyzedInstructions'),
            cheap=recipe_data.get('cheap'),
            creditsText=recipe_data.get('creditsText'),
            cuisines=recipe_data.get('cuisines'),
            dairyFree=recipe_data.get('dairyFree'),
            diets=recipe_data.get('diets'),
            gaps=recipe_data.get('gaps'),
            glutenFree=recipe_data.get('glutenFree'),
            ketogenic=recipe_data.get('ketogenic'),
            lowFodmap=recipe_data.get('lowFodmap'),
            occasions=recipe_data.get('occasions'),
            sustainable=recipe_data.get('sustainable'),
            vegan=recipe_data.get('vegan'),
            vegetarian=recipe_data.get('vegetarian'),
            veryHealthy=recipe_data.get('veryHealthy'),
            veryPopular=recipe_data.get('veryPopular'),
            whole30=recipe_data.get('whole30'),
            weightWatcherSmartPoints=recipe_data.get('weightWatcherSmartPoints'),
            dishTypes=recipe_data.get('dishTypes'),
            extendedIngredients=recipe_data.get('extendedIngredients'),
            summary=recipe_data.get('summary'),
            winePairing=recipe_data.get('winePairing')
        )

        # Add ingredients to the recipe (if provided)
        ingredients_data = recipe_data.get('extendedIngredients')
        if ingredients_data:
            for ingredient_data in ingredients_data:
                # Extract ingredient_id and amount from ingredient_data
                ingredient_id = ingredient_data.get('id')
                amount = ingredient_data.get('amount')

                # Call the get_ingredient_info view using requests
                url = f'https://localhost:8000/api/get_ingredient_info/{ingredient_id}/{amount}/'

                try:
                    response = requests.get(url)
                    response.raise_for_status()  # Raise an exception for non-2xx responses

                    # Process the response as needed (e.g., print response content)
                    print(response.content)

                except requests.RequestException as e:
                    print(f"Error fetching ingredient information: {e}")
                

        return recipe

