import pytest
from rest_framework.test import APIClient
from rest_framework import status
from datetime import date

@pytest.mark.django_db
@pytest.mark.parametrize(
    "username, password, gender, email, weight, height, date_of_birth, activityLevel, expected_valid",
    [
        ("short", "valid_password", "Male", "valid@example.com", 80.0, 170.0, "2000-01-01", 1, False),  # Invalid username: shorter than 6 characters
        ("valid_username", "short", "Male", "valid@example.com", 80.0, 170.0, "2000-01-01", 1, False),  # Invalid password: shorter than 6 characters
        ("valid_username", "valid_password", "Male", "invalid_email", 80.0, 170.0, "2000-01-01", 1, False),  # Invalid email: incorrect format
        ("valid_username", "valid_password", "Male", "valid@example.com", -5.0, 170.0, "2000-01-01", 1, False),  # Invalid weight: negative value
        ("valid_username", "valid_password", "Male", "valid@example.com", 80.0, -170.0, "2000-01-01", 1, False),  # Invalid height: negative value
    ]
)
def test_create_user_profile(username, password, gender, email, weight, height, date_of_birth, activityLevel, expected_valid):
    client = APIClient()

    # Define test data
    data = {
        "username": username,
        "password": password,
        "gender": gender,
        "email": email,
        "weight": weight,
        "height": height,
        "date_of_birth": date_of_birth,
        "activityLevel": activityLevel
    }

    # Make a POST request to create a new user profile
    response = client.post('/user/api/v1/user/', data, format='json')

    if expected_valid:
        assert response.status_code == status.HTTP_201_CREATED
        # Add more assertions if needed
    else:
        assert response.status_code != status.HTTP_201_CREATED
        # Add more assertions if needed
