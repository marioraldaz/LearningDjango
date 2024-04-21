from django.urls import path
from .views.view_ingredient import IngredientView
from .views.view_recipe import RecipeView

urlpatterns = [
    path('ingredient/save/', IngredientView().post, name='save_ingredient'),
    path('ingredient/save-nutrition/', IngredientView().save_nutrition, name='save_nutrition'),
    path('recipe/save/', RecipeView().post, name='save_recipe'),
    path('recipe/save-extended-ingredients/', RecipeView().save_extended_ingredients, name='save_extended_ingredients'),
    path('recipe/save-nutrition/', RecipeView().save_nutrition, name='save_recipe_nutrition'),
]
