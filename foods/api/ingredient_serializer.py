from rest_framework import serializers
from ..nutrition import  Nutrition
from ..ingredient import Ingredient
from ..recipe import Nutrition


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

    @classmethod
    def create(cls, validated_data):
        return Ingredient.objects.create(**validated_data)