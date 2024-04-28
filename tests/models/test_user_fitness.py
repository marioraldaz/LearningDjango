from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.user_profile import UserProfile
from profiles.profile_fitness import  UserFitnessProfile

import json

class TestFitnessProfileView(TestCase):

    def setUp(self):
        # Create a test user and associated profiles
        self.user = User.objects.create_user(username='testuser', password='password')
        self.user_profile = UserProfile.objects.create(user=self.user)
        self.fitness_profile = UserFitnessProfile.objects.create(user_profile=self.user_profile)

    def test_fitness_profile_view_GET(self):
        # Test GET request to the fitness_profile view
        self.client.force_login(self.user)
        response = self.client.get(reverse('fitness_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'fitness_profile.html')

    def test_fitness_profile_view_POST(self):
        # Test POST request to the fitness_profile view
        self.client.force_login(self.user)
        url = reverse('fitness_profile')
        data = {
            'goal': 'Lose',
            'activityLevel': 2
        }
        response = self.client.post(url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

        # Verify that fitness profile fields are updated
        self.fitness_profile.refresh_from_db()
        self.assertEqual(self.fitness_profile.goal, 'Lose')
        self.assertEqual(self.fitness_profile.activity_level, 2)

    def test_fitness_profile_view_invalid_JSON(self):
        # Test POST request with invalid JSON payload
        self.client.force_login(self.user)
        url = reverse('fitness_profile')
        invalid_data = '{invalid-json}'  # Invalid JSON payload
        response = self.client.post(url, data=invalid_data, content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_fitness_profile_view_unauthenticated(self):
        # Test access to the fitness_profile view without authentication
        url = reverse('fitness_profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)  # Redirect to login page (status code 302)

    # Add more tests as needed to cover additional scenarios
