from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.conf import settings
import requests

API_KEY = settings.API_KEY

@require_GET
def fetch_filtered_recipes(request):
    try:
        query_params = request.GET.urlencode()
        url = f"https://api.spoonacular.com/recipes/complexSearch?apiKey={API_KEY}&{query_params}"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        return JsonResponse(data['results'], safe=False)
    except requests.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)

@require_GET
def get_recipe_info(request, id):
    try:
        url = f"https://api.spoonacular.com/recipes/{id}/information?apiKey={API_KEY}"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        return JsonResponse(data)
    except requests.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)

@require_GET
def fetch_recipes_by_name(request, name):
    try:
        url = f"https://api.spoonacular.com/recipes/complexSearch?apiKey={API_KEY}&query={name}&sort=popularity"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        return JsonResponse(data['results'], safe=False)
    except requests.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)

@require_GET
def get_recipe_by_id(request, recipe_id):
    try:
        url = f"https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={API_KEY}&includeNutrition=true"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        return JsonResponse(data)
    except requests.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)
