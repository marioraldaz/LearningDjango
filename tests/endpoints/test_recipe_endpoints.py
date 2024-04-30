import pytest
from django.urls import reverse
from rest_framework import status

from django.conf import settings


#######################################################   Tests on my endpoints #################################################
@pytest.mark.recipes
@pytest.mark.spoonacular_api
@pytest.mark.django_db
@pytest.mark.django_db
def test_fetch_recipes_by_name(client):
    # Construct the URL for the view, including the 'name' parameter
    url = reverse('fetch_recipes_by_name', kwargs={'name': 'chicken'})

    # Make a GET request to the endpoint
    response = client.get(url)

    # Assert the response status code
    assert response.status_code == status.HTTP_200_OK
    
@pytest.mark.recipes
@pytest.mark.spoonacular_api
@pytest.mark.django_db
def test_get_recipe_info(client):
    url = reverse('get_recipe_info', kwargs={'id': 123})
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    
@pytest.mark.recipes
@pytest.mark.spoonacular_api
@pytest.mark.django_db
def test_fetch_filtered_recipes(client):
    url = reverse('fetch_filtered_recipes')
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.recipes
@pytest.mark.spoonacular_api
@pytest.mark.django_db
def test_get_recipe_by_id(client):
    url = reverse('get_recipe_by_id', kwargs={'recipe_id': 200})
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    
#######################################################################################################################################