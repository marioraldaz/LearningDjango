from rest_framework import serializers
from ..user_profile import UserProfile
from ..food import Food
from ..food_intake import FoodIntake
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

class FoodIntakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodIntake
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
    
    
    
from ..food_intake import FoodIntake
from ..food_intake_detail import FoodIntakeDetail

class FoodIntakeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodIntakeDetail
        fields = '__all__'  # You can specify specific fields if needed

class FoodIntakeSerializer(serializers.ModelSerializer):
    intake_details = FoodIntakeDetailSerializer(many=True, read_only=True)

    class Meta:
        model = FoodIntake
        fields = ['id', 'profile', 'meal_type', 'intake_date', 'intake_details']

class FoodIntakeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodIntakeDetail
        fields = '__all__'