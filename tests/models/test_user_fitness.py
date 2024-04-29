from django.test import TestCase
from django.urls import reverse
from profiles.profile_fitness import UserFitnessProfile
from django.shortcuts import get_object_or_404
import pytest
import json


@pytest.fixture
def client_logged_in(client, user):
    # Log in the client with the test userr
    client.force_login(user)
    return client

def test_fitness_profile_view_authenticated_GET(client_logged_in):
    # Test GET request to the fitness_profile view with authentication
    response = client_logged_in.get(reverse('fitness_profile'))
    assert response.status_code == 200
    assert 'fitness_profile.html' in [t.name for t in response.templates]

def test_fitness_profile_view_authenticated_POST(client_logged_in, user_profile):
    # Test POST request to the fitness_profile view with authentication
    url = reverse('fitness_profile')
    data = {
        'goal': 'Lose',
        'activityLevel': 2
    }
    response = client_logged_in.post(url, data=json.dumps(data), content_type='application/json')
    assert response.status_code == 200

    # Refresh fitness profile from the database and verify updated fields
    fitness_profile = get_object_or_404(UserFitnessProfile, user_profile=user_profile)
    assert fitness_profile.goal == 'Lose'
    assert fitness_profile.activity_level == 2

def test_fitness_profile_view_invalid_JSON(client_logged_in):
    # Test POST request with invalid JSON payload
    url = reverse('fitness_profile')
    invalid_data = '{invalid-json}'  # Invalid JSON payload
    response = client_logged_in.post(url, data=invalid_data, content_type='application/json')
    assert response.status_code == 400

def test_fitness_profile_view_unauthenticated(client):
    # Test access to the fitness_profile view without authentication
    url = reverse('fitness_profile')
    response = client.get(url)
    assert response.status_code == 302  # Redirect to login page (status code 302)