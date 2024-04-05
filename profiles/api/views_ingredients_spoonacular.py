import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.conf import settings
 
API_KEY = settings.API_KEY

@api_view(['GET'])
def fetch_ingredients_by_name(request, name):
    try:
        url = f"https://api.spoonacular.com/food/ingredients/search"
        params = {'apiKey': API_KEY, 'query': name}
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        return Response(data['results'])
    except requests.RequestException as e:
        return Response({'error': str(e)}, status=500)

@api_view(['GET'])
def get_ingredient_details(request, ingredient_id, amount):
    try:
        url = f"https://api.spoonacular.com/food/ingredients/{ingredient_id}/information"
        params = {'apiKey': API_KEY, 'amount': amount}
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        return Response(data)
    except requests.RequestException as e:
        return Response({'error': str(e)}, status=500)

@api_view(['GET'])
def fetch_filtered_ingredients(request):
    try:
        url = "https://api.spoonacular.com/food/ingredients/search"
        params = request.query_params.dict()
        params['apiKey'] = API_KEY
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        return Response(data['results'])
    except requests.RequestException as e:
        return Response({'error': str(e)}, status=500)
