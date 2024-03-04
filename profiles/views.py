from rest_framework import viewsets
from .serializer import UserSerializer
from .user import User
from .food import Food
from .food_intake import UserFoodIntake
from .allergies import Allergy
from .savedRecipe import SavedRecipe
from .user_recipe import UserRecipe
from django.contrib import admin


from .serializer import (
    UserSerializer,
    FoodSerializer,
    UserFoodIntakeSerializer,
    AllergySerializer,
    SavedRecipeSerializer,
    UserRecipeSerializer
)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class UserFoodIntakeViewSet(viewsets.ModelViewSet):
    queryset = UserFoodIntake.objects.all()
    serializer_class = UserFoodIntakeSerializer

class AllergyViewSet(viewsets.ModelViewSet):
    queryset = Allergy.objects.all()
    serializer_class = AllergySerializer

class SavedRecipeViewSet(viewsets.ModelViewSet):
    queryset = SavedRecipe.objects.all()
    serializer_class = SavedRecipeSerializer

class UserRecipeViewSet(viewsets.ModelViewSet):
    queryset = UserRecipe.objects.all()
    serializer_class = UserRecipeSerializer

