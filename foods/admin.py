from django.contrib import admin

from food_intake.nutrition_stats import NutritionStats
from foods.ingredient import Ingredient
from foods.nutrition import Nutrition
from foods.recipe import Recipe


admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(Nutrition)
admin.site.register(NutritionStats)