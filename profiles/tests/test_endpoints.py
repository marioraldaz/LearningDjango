# test_views.py

import pytest
from django.urls import reverse
from ..factories.profile_factory import ProfileFactory  # Import your UserProfile factory
from django.utils import timezone

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
