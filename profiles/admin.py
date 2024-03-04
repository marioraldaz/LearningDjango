from django.contrib import admin
from .user import User
from .food import Food
from .food_intake import UserFoodIntake
from .allergies import Allergy
from .savedRecipe import SavedRecipe
from .user_recipe import UserRecipe

# Register your models here.

admin.site.register(User)
admin.site.register(Food)
admin.site.register(UserFoodIntake)
admin.site.register(Allergy)
admin.site.register(SavedRecipe)
admin.site.register(UserRecipe)
