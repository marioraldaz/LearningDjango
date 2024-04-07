from django.conf import settings
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def fetch_ingredients_by_name(request, name):
    try:
        api_key = settings.API_KEY
        url = f"https://api.spoonacular.com/food/ingredients/search"
        params = {'apiKey': api_key, 'query': name}
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        return Response(data['results'])
    except requests.RequestException as e:
        return Response({'error': str(e)}, status=500)

@api_view(['GET'])
def fetch_ingredient_by_id(request, ingredient_id, amount):
    try:
        api_key = settings.API_KEY
        url = f"https://api.spoonacular.com/food/ingredients/{ingredient_id}/information"
        params = {'apiKey': api_key, 'amount': amount}
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        return Response(data)
    except requests.RequestException as e:
        return Response({'error': str(e)}, status=500)


@api_view(['GET'])
def fetch_filtered_recipes(request):
    try:
        api_key = settings.API_KEY  
        url = "https://api.spoonacular.com/recipes/complexSearch"
        params = request.query_params.dict()
        params['apiKey'] = api_key
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        return Response(data['results'])
    except requests.RequestException as e:
        return Response({'error': str(e)}, status=500)
