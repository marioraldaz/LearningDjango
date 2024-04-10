import requests
import pytest
from django.urls import reverse
from rest_framework import status

from django.conf import settings

API_KEY = settings.API_KEY


###############################################  Functions  ###################################################

def fetch_recipe_from_spoonacular(url):
    response = requests.get(url)
    return response

#################################################################################################################



################################################ Tests Directly into the API #########################################################

@pytest.mark.ingredients
@pytest.mark.spoonacular_api
@pytest.mark.parametrize("url, expected_response", [
    (
        f"https://api.spoonacular.com/food/ingredients/search?query=banana&number=2&sort=calories&sortDirection=desc&apiKey={API_KEY}",
        {
            "results": [
                {"id": 19400, "name": "banana chips", "image": "banana-chips.jpg"},
                {"id": 93671, "name": "banana bread mix", "image": "banana-bread.jpg"}
            ],
            "offset": 0,
            "number": 2,
            "totalResults": 14
        }
    ),
    (
        f"https://api.spoonacular.com/food/ingredients/search?query=apple&number=4&sort=calories&sortDirection=asc&apiKey={API_KEY}",
        {
            "results": [
                {"id": 2048, "name": "apple cider vinegar", "image": "apple-cider-vinegar.jpg"},
                {"id": 9312, "name": "rose apple", "image": "rose-apples.jpg"},
                {"id": 99171, "name": "star apple", "image": "star-apple.jpg"},
                {"id": 9019, "name": "applesauce", "image": "applesauce.png"}
            ],
            "offset": 0,
            "number": 4,
            "totalResults": 39
        }
    ),
])

@pytest.mark.ingredients
@pytest.mark.spoonacular_api
def test_fetch_recipe_from_spoonacular(monkeypatch, url, expected_response):
    # Define a mock function to replace requests.get
    def mock_get(url):
        return expected_response

    # Patch requests.get with the mock function
    monkeypatch.setattr(requests, "get", mock_get)

    # Call the function under test with the provided URL
    result = fetch_recipe_from_spoonacular(url)

    # Assert that the result matches the expected response
    assert result == expected_response


