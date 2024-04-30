import pytest
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    """Fixture for creating an instance of the Django test client."""
    return APIClient()


@pytest.mark.django_db
def test_save_recipe_url(api_client, recipe_factory):
    recipe = recipe_factory.create()  # Use build() to create an instance without saving to DB
    url = reverse('save_recipe')
    response = api_client.post(url, data=recipe.__dict__, format='json')
    assert response.status_code == 201  # Check if the recipe is successfully saved (status code 201)
    assert response.data['title'] == recipe.title  # Optionally check other attributes if needed

@pytest.mark.django_db
def test_fetch_filtered_ingredients_url(api_client, ingredient_factory):
    ingredient = ingredient_factory.create()  # Use build() to create an instance without saving to DB
    url = reverse('fetch_filtered_ingredients')
    response = api_client.get(url, data={'category': ingredient.category})
    assert response.status_code == 200  # Check if ingredients are fetched successfully (status code 200)

@pytest.mark.django_db
def test_get_ingredient_info_url(api_client, ingredient_factory):
    ingredient = ingredient_factory.create()  # Use create() to create and save an instance to DB
    url = reverse('get_ingredient_details', args=[ingredient.id, 100])  # Assuming amount=100
    response = api_client.get(url)
    assert response.status_code == 200  # Check if ingredient details are retrieved successfully (status code 200)

# Add similar tests for other views and URLs using the factories