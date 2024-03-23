from django.contrib import admin
from .user_profile import UserProfile
from .food import Food
from .food_intake import FoodIntake
from .allergies import Allergy
from .saved_recipes import SavedRecipe
from .user_recipe import UserRecipe

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Food)
admin.site.register(FoodIntake)
admin.site.register(Allergy)
admin.site.register(SavedRecipe)
admin.site.register(UserRecipe)
