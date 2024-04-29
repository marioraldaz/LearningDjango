import pytest
from rest_framework import status

from factories.user_profile_factory import UserProfileFactory
from rest_framework.test import APIClient
from django.urls import reverse
from factories.user_daily_factory import UserDailyFactory
from food_intake.user_daily import UserDaily

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user_profile():
    return UserProfileFactory()

@pytest.fixture
def user_daily(user_profile):
    return UserDailyFactory(profile=user_profile)

@pytest.mark.django_db
def test_get_user_dailies(api_client, user_profile, user_daily):
    url = reverse('user_dailies', kwargs={'profile_id': user_profile.id})
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1  # Expecting one UserDaily object associated with the user_profile

@pytest.mark.django_db
def test_create_user_daily(api_client, user_profile):
    url = reverse('user_dailies', kwargs={'profile_id': user_profile.id})
    data = {'date': '2024-05-01'}  # Sample data for creating a UserDaily object
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED

@pytest.mark.django_db
def test_delete_user_daily(api_client, user_profile, user_daily):
    url = reverse('user_daily_detail', kwargs={'profile_id': user_profile.id, 'pk': user_daily.id})
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not UserDaily.objects.filter(pk=user_daily.id).exists()  # Ensure the UserDaily object is deleted