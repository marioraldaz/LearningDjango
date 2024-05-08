from rest_framework import serializers
from ..models import *

class FoodIntakeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodIntakeDetail
        fields = '__all__'  # You can specify specific fields if needed

class FoodIntakeSerializer(serializers.ModelSerializer):
    intake_details = FoodIntakeDetailSerializer(many=True, read_only=True)
    
    class Meta:
        model = FoodIntake
        fields = '__all__'

class FoodIntakeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodIntakeDetail
        fields = '__all__'
        
class FoodIntakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodIntake
        fields = '__all__'

class UserDailySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDaily
        fields = '__all__'
        
class NutritionStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NutritionStats
        fields = '__all__'