from rest_framework import serializers
from ..user_profile import UserProfile
from ..food import Food
from ..food_intake import UserFoodIntake
from ..allergies import Allergy
from ..saved_recipes import SavedRecipe
from ..user_recipe import UserRecipe

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
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

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer