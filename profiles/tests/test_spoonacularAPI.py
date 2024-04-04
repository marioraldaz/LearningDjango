import pytest
import requests

# Define the base URL of your external API
BASE_URL = 'https://api.example.com'

@pytest.mark.parametrize("endpoint", ["/users", "/posts", "/comments"])
def test_api_endpoint(endpoint):
    # Send a GET request to the API endpoint
    response = requests.get(f"{BASE_URL}{endpoint}")

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Example: Assert the response content (you can customize this based on your API)
    assert isinstance(response.json(), list)

    # Example: Assert specific data in the response JSON
    if endpoint == "/users":
        assert len(response.json()) > 0  # Assuming users endpoint should return a non-empty list

    # Add more assertions based on your API's behavior and response structure

# Add more test functions as needed to cover different endpoints and scenarios
