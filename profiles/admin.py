from django.contrib import admin
from .user_profile import UserProfile
from .allergies import Allergy
from .saved_recipes import SavedRecipe
from ..foods.recipe import UserRecipe
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Allergy)
admin.site.register(SavedRecipe)
admin.site.register(UserRecipe)
