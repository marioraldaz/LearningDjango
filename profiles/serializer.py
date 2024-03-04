from rest_framework import serializers
from .user import User

from rest_framework import serializers
from .user import User
from .food import Food
from .food_intake import UserFoodIntake
from .allergies import Allergy
from .savedRecipe import SavedRecipe
from .user_recipe import UserRecipe

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'

class UserFoodIntakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFoodIntake
        fields = '__all__'

class AllergySerializer(serializers.ModelSerializer):
    class Meta:
        model = Allergy
        fields = '__all__'

class SavedRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedRecipe
        fields = '__all__'

class UserRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRecipe
        fields = '__all__'
