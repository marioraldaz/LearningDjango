import pytest
from django.urls import reverse
from ...food_intake import FoodIntake
from ...factories.food_intake_factory import FoodIntakeFactory


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

""""
@pytest.mark.django_db
def test_food_intake_detail(client, create_food_intake_and_detail):
    # Access the created FoodIntake and FoodIntakeDetail instances via the fixture
    food_intake, food_intake_detail = create_food_intake_and_detail
    pass
    # Test GET request
    url = reverse('food_intake_detail', kwargs={'pk': food_intake_detail.pk})
    response = client.get(url)
    assert response.status_code == 200

    # Ensure the response contains the expected keys and values
    response_data = response.json()
    assert 'id' in response_data
    assert 'food_intake' in response_data
    assert 'item_name' in response_data
    assert 'item_type' in response_data

    # Assert on specific values if needed
    assert response_data['item_name'] == 'Chips'  # Assuming 'Chips' is the expected value
    assert response_data['item_type'] == 'Ingredient'  # Assuming 'Ingredient' is the expected value
"""


    
@pytest.mark.django_db
def test_save_food_intake(client, create_user_profile):
    # Access the created user profile
    user_profile = create_user_profile

    # Test POST request
    url = reverse('save_food_intake')
    data = {'meal_type': 'Breakfast', 'intake_date': '2024-01-01', 'profile_id': user_profile.pk}
    response = client.post(url, data)
    print(response.content)
    assert response.status_code == 200
    assert FoodIntake.objects.filter(meal_type='Breakfast').exists()
    


@pytest.mark.django_db
def test_food_intake_creation():
    intake = FoodIntakeFactory()
    assert FoodIntake.objects.count() == 1
    assert intake.profile is not None