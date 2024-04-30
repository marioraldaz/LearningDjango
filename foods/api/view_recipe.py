from django.conf import settings
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..recipe import Recipe
from .recipe_serializer import RecipeSerializer
from ..nutrition import Nutrition
from django.views.decorators.http import require_POST
import json
from django.http import HttpResponseServerError


def save_recipe(request):
    try:
        # Deserialize the JSON data from the request body into a Recipe object
        recipe_data = json.loads(request.body)
        serializer = RecipeSerializer(data=recipe_data)
        if serializer.is_valid():
            # Save the validated Recipe object to the database
            serializer.save()
            return Response(serializer.data, status=201)  # Return the serialized Recipe object
        else:
            return Response(serializer.errors, status=400)  # Return validation errors
    except Exception as e:
        return Response({'error': str(e)}, status=500)  # Return any other errors

def get_recipe_info(request, recipe_id):

    # Check if a recipe with the same spoonacular_id already exists
    existing_recipe = Recipe.objects.filter(spoonacular_id=recipe_id).first()
    
    if existing_recipe:
        # If the recipe exists, serialize it and return it
        serialized_recipe = RecipeSerializer(existing_recipe).data
        return Response(serialized_recipe)
    
    
    url = f'https://api.spoonacular.com/recipes/{recipe_id}/information'
    params = {
        'api_key' : settings.API_KEY
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise exception for any error status codes
        data = response.json()
        
        # Extract necessary data from Spoonacular API response
        nutrition_data = data.get('nutrition', {})  # Assuming nutrition data is nested under 'nutrition' key
        ingredients_data = data.get('extendedIngredients', [])  # Assuming ingredients data is nested under 'extendedIngredients' key
        
        # Create Nutrition object
        nutrition = Nutrition.objects.create(**nutrition_data)

        # Create Recipe object
        recipe_data = {
            'nutrition': nutrition,
            'title': data.get('title'),
            'image': data.get('image'),
            'readyInMinutes': data.get('readyInMinutes'),
            'instructions': data.get('instructions'),
            'spoonacular_id': data.get('id'),
            'sourceName': data.get('sourceName'),
            'sourceUrl': data.get('sourceUrl'),
            'healthScore': data.get('healthScore'),
            'spoonacularScore': data.get('spoonacularScore'),
            'pricePerServing': data.get('pricePerServing'),
            'analyzedInstructions': data.get('analyzedInstructions'),
            'cheap': data.get('cheap'),
            'creditsText': data.get('creditsText'),
            'cuisines': data.get('cuisines'),
            'dairyFree': data.get('dairyFree'),
            'diets': data.get('diets'),
            'gaps': data.get('gaps'),
            'glutenFree': data.get('glutenFree'),
            'instructions': data.get('instructions'),
            'ketogenic': data.get('ketogenic'),
            'lowFodmap': data.get('lowFodmap'),
            'occasions': data.get('occasions'),
            'sustainable': data.get('sustainable'),
            'vegan': data.get('vegan'),
            'vegetarian': data.get('vegetarian'),
            'veryHealthy': data.get('veryHealthy'),
            'veryPopular': data.get('veryPopular'),
            'whole30': data.get('whole30'),
            'weightWatcherSmartPoints': data.get('weightWatcherSmartPoints'),
            'dishTypes': data.get('dishTypes'),
            'extendedIngredients': ingredients_data,
            'summary': data.get('summary'),
            'winePairing': data.get('winePairing'),
        }

        recipe = Recipe.objects.create(**recipe_data)
        
        # Serialize the recipe data
        serialized_recipe = RecipeSerializer(recipe).data
        return Response(serialized_recipe)
    except requests.RequestException as e:
        return Response({'error': str(e)}, status=500)
    

def fetch_filtered_recipes(request):
    filters = request.GET.dict()
    url = f'https://api.spoonacular.com/complexSearch'
    params = {
        'apiKey': settings.API_KEY,
        **filters  # Pass the filters as URL parameters
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise exception for any error status codes
        data = response.json()
        return Response(data)
    except requests.RequestException as e:
        return Response({'error': str(e)}, status=500)

import json
import requests
from django.conf import settings
from django.http import JsonResponse, HttpResponseServerError

def fetch_recipes_by_name(request, name):
    url = 'https://api.spoonacular.com/recipes/complexSearch'
    params = {
        'apiKey': settings.API_KEY,
        'query': name,
        'number': 10  # Adjust this value to specify the number of results to fetch
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise exception for any error status codes

        data = response.json()
        recipes = data.get('results', [])

        if not recipes:
            return JsonResponse({'error': 'No recipes found for the given name'}, status=404)

        # Serialize recipes list to JSON string
        serialized_recipes = json.dumps(recipes)
        return JsonResponse(serialized_recipes, safe=False)  # Use safe=False to allow non-dict objects

    except requests.RequestException as e:
        return HttpResponseServerError(json.dumps({'error': str(e)}))