import pytest
from django.urls import reverse
from ..food_intake import FoodIntake
from ..user_profile import UserProfile

@pytest.fixture
def create_user_profile():
    user_profile = UserProfile.objects.create(
        username='test_user',
        password='test_password',
        gender='Male',  # or 'Female'
        email='test@example.com',
        weight=70,
        height=180,
        date_of_birth='2000-01-01',
        activityLevel=1
    )
    yield user_profile
    user_profile.delete()  # Clean up after the test


@pytest.mark.django_db
def test_food_intake_list(client, create_user_profile):
    # Access the created user profile
    user_profile = create_user_profile

    # Create some sample data
    FoodIntake.objects.create(meal_type='Breakfast', intake_date='2024-04-01', profile=user_profile)
    FoodIntake.objects.create(meal_type='Lunch', intake_date='2024-04-02', profile=user_profile)

    # Test GET request
    url = reverse('food_intake_list')
    response = client.get(url)
    assert response.status_code == 200  

    # Test POST request
    data = {'meal_type': 'Dinner', 'intake_date': '2024-04-03', 'profile': user_profile.pk}
    response = client.post(url, data)
    assert response.status_code == 201
    assert FoodIntake.objects.filter(meal_type='Dinner').exists()

@pytest.mark.django_db
def test_food_intake_detail(client, create_user_profile):
    # Access the created user profile
    user_profile = create_user_profile

    # Create a sample FoodIntake object
    food_intake = FoodIntake.objects.create(meal_type='Snack', intake_date='2024-04-04', profile=user_profile)

    # Test GET request
    url = reverse('food_intake_detail', kwargs={'pk': food_intake.pk})
    response = client.get(url)
    assert response.status_code == 200
    assert response.json()['meal_type'] == 'Snack'

    # Test PUT request
    updated_data = {'meal_type': 'Updated Snack', 'profile': user_profile.pk}
    response = client.put(url, updated_data)
    assert response.status_code == 200
    assert FoodIntake.objects.get(pk=food_intake.pk).meal_type == 'Updated Snack'

    # Test DELETE request
    response = client.delete(url)
    assert response.status_code == 204
    assert not FoodIntake.objects.filter(pk=food_intake.pk).exists()

@pytest.mark.django_db
def test_save_food_intake(client):
    # Test POST request
    url = reverse('save_food_intake')
    data = {'meal_type': 'Breakfast', 'intake_date': '2024-01-01', 'profile_id': 5}
    response = client.post(url, data)
    assert response.status_code == 200
    assert FoodIntake.objects.filter(meal_type='Breakfast').exists()
