import pytest
from django.urls import reverse
from ..factories.profile_factory import ProfileFactory 
from django.utils import timezone
from ..factories.food_intake_factory import FoodIntakeFactory
from django.shortcuts import HttpResponse

@pytest.mark.django_db
def test_save_food_intake(client):
    user_profile = ProfileFactory()  # Create a user profile using the factory
    url = reverse('save_food_intake')  # Assuming 'save_food_intake' is the name of your URL pattern
    intake_data = {
        'meal_type': 'Breakfast',
        'intake_date': timezone.now().date(),  # Use today's date
        'profile_id': user_profile.id  # Pass the user profile ID
    }

    # Use the Django test client to simulate a POST request to your endpoint
    response = client.post(url, intake_data)

    # Assert that the response is as expected
    assert response.status_code == 200
    assert 'success' in response.json()
    assert response.json()['success'] is True
    assert 'message' in response.json()
    assert response.json()['message'] == 'Food intake saved successfully'

@pytest.mark.django_db
def test_food_intake_list(client):
    # Create some food intake instances using the factory
    FoodIntakeFactory.create_batch(5)

    # Get the URL for the food_intake_list view
    url = reverse('food_intake_list')

    # Make a GET request to the URL using the test client
    response = client.get(url)

    # Check that the response status code is 200 OK
    assert response.status_code == HttpResponse.status_code

    # Check other assertions as needed based on your view's behavior
    assert len(response.content) > 0  # Assuming the response has content
    # Add more assertions as needed

@pytest.mark.django_db
def test_food_intake_detail(client):
    # Create a food intake instance using the factory
    food_intake = FoodIntakeFactory()

    # Get the URL for the food_intake_detail view with the food intake's pk
    url = reverse('food_intake_detail', kwargs={'pk': food_intake.pk})

    # Make a GET request to the URL using the test client
    response = client.get(url)

    # Check that the response status code is 200 OK
    assert response.status_code == HttpResponse.status_code

    # Check other assertions as needed based on your view's behavior
    assert len(response.content) > 0  # Assuming the response has content
    # Add more assertions as needed