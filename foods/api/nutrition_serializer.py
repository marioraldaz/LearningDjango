from rest_framework import serializers
from ..nutrition import Nutrition
        

class NutritionSerializer(serializers.ModelSerializer):
    """Serializer for the Nutrition model."""

    class Meta:
        model = Nutrition
        fields = ('calories', 'carbs', 'fat', 'protein')