from rest_framework import serializers
from ..ingredient import Ingredient
from ..recipe import Recipe

        
class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'

    def create(self, validated_data):
        ingredients_data = validated_data.pop('extendedIngredients')
        recipe = Recipe.objects.create(**validated_data)
        # Assuming you have a method to handle adding ingredients to the recipe
        recipe.add_ingredients(ingredients_data)
        return recipe
