from django.conf import settings
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..recipe import Recipe
from .recipe_serializer import RecipeSerializer
from ..nutrition import Nutrition
from django.views.decorators.http import require_POST
from .ingredient_serializer import IngredientSerializer
import json
from ..ingredient import Ingredient
from rest_framework.views import APIView
from django.http import JsonResponse

class IngredientView(APIView):
    
    def save_ingredient(self,request):
        # This code snippet is a method named `save_ingredient` within a class named `IngredientView`.
        # Here's a breakdown of what the code is doing:
        try:
            # Deserialize the JSON data from the request body into an Ingredient object
            ingredient_data = json.loads(request.body)
            serializer = IngredientSerializer(data=ingredient_data)
            if serializer.is_valid():
                # Save the validated Ingredient object to the database
                serializer.save()
                return JsonResponse(serializer.data, status=201)  # Return the serialized Ingredient object
            else:
                return JsonResponse(serializer.errors, status=400)  # Return validation errors
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)  # Return any other errors
        
        
    def get_ingredient_info(self, request, id, amount):
        try:
            # Check if an ingredient with the same spoonacular_id already exists
            existing_ingredient = Ingredient.objects.filter(spoonacular_id=id).first()
            
            if existing_ingredient:
                # If the ingredient exists, serialize it and return it
                serialized_ingredient = IngredientSerializer(existing_ingredient).data
                return JsonResponse(serialized_ingredient)
            
            # If the ingredient doesn't exist, fetch it from Spoonacular API
            url = f'https://api.spoonacular.com/food/ingredients/{id}/information'
            params = {
                'apiKey': settings.API_KEY
            }
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise exception for any error status codes
            data = response.json()
            
            # Extract necessary data from Spoonacular API response
            nutrition_data = data.get('nutrition', {})  # Assuming nutrition data is nested under 'nutrition' key
            
            # Create Nutrition object
            nutrition = Nutrition.objects.create(**nutrition_data)

            # Create Ingredient object
            ingredient_data = {
                'nutrition': nutrition,
                'name': data.get('name'),
                'spoonacular_id': data.get('id'),
                'original': data.get('original'),
                'originalName': data.get('originalName'),
                'amount': data.get('amount'),
                'unit': data.get('unit'),
                'unitShort': data.get('unitShort'),
                'unitLong': data.get('unitLong'),
                'possibleUnits': data.get('possibleUnits'),
                'estimatedCost_value': data.get('estimatedCost', {}).get('value'),
                'estimatedCost_unit': data.get('estimatedCost', {}).get('unit'),
                'consistency': data.get('consistency'),
                'shoppingListUnits': data.get('shoppingListUnits'),
                'aisle': data.get('aisle'),
                'image': data.get('image'),
                'meta': data.get('meta'),
                'categoryPath': data.get('categoryPath'),
            }

            ingredient = Ingredient.objects.create(**ingredient_data)
            
            # Serialize the ingredient data
            serialized_ingredient = IngredientSerializer(ingredient).data
            return JsonResponse(serialized_ingredient)
        except requests.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)

    
    def fetch_ingredients_by_name(self, request, name):
        try:
            # Construct the API URL
            url = f'https://api.spoonacular.com/food/ingredients/search'
            
            # Set query parameters
            params = {
                'apiKey': settings.API_KEY,
                'query': name  # Access 'name' parameter from request query parameters
            }
            
            # Send GET request to the API
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise exception for any error status codes
            
            # Parse the JSON response
            data = response.json()
            
            # Extract the list of ingredients
            ingredients = data.get('results', [])
            
            # Return the list of ingredients as JSON response
            return JsonResponse(ingredients, safe=False)
        except requests.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)
            
    def fetch_filtered_ingredients(self, request):
        try:
            # Construct the API URL
            url = 'https://api.spoonacular.com/food/ingredients/search'
            
            # Get filters from request query parameters
            filters = request.query_params
            
            # Add API key to filters
            filters['apiKey'] = settings.API_KEY
            
            # Send GET request to the API
            response = requests.get(url, params=filters)
            response.raise_for_status()  # Raise exception for any error status codes
            
            # Parse the JSON response
            data = response.json()
            
            # Extract the list of ingredients
            ingredients = data.get('results', [])
            
            # Return the list of ingredients as JSON response
            return JsonResponse(ingredients)
        except requests.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)