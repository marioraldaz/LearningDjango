import requests
import pytest

API_KEY = "8347c0a7ffc148269108ea0a29f1509e"



def fetch_recipe_from_spoonacular():
    
    url = f" https://api.spoonacular.com/food/ingredients/search?query=banana&number=2&sort=calories&sortDirection=desc&apiKey={API_KEY}"
    response = requests.get(url)
    return response

@pytest.mark.spoonacular_api
def test_fetch_recipe_from_spoonacular(monkeypatch):
    # Define a mock response with the expected data
    mock_response = {
        "results": [
            {"id": 19400, "name": "banana chips", "image": "banana-chips.jpg"},
            {"id": 93671, "name": "banana bread mix", "image": "banana-bread.jpg"}
        ],
        "offset": 0,
        "number": 2,
        "totalResults": 14
    }

    # Define a mock function to replace requests.get
    def mock_get(url):
        return mock_response

    # Patch requests.get with the mock function
    monkeypatch.setattr(requests, "get", mock_get)

    # Call the function under test
    result = fetch_recipe_from_spoonacular()

    # Assert that the result matches the mock response
    assert result == mock_response