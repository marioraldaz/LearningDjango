import pytest
from django.urls import reverse
from ..food_intake import FoodIntake
from ..food_intake_detail import FoodIntakeDetail
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
    

@pytest.fixture
def create_food_intake_and_detail(create_user_profile):
    # Access the created user profile using the create_user_profile fixture
    user_profile = create_user_profile

    # Create a sample FoodIntake object associated with the user profile
    food_intake = FoodIntake.objects.create(
        meal_type='Snack',
        intake_date='2024-04-04',
        profile=user_profile
    )

    # Create a sample FoodIntakeDetail object associated with the FoodIntake
    food_intake_detail = FoodIntakeDetail.objects.create(
        food_intake=food_intake,
        item_name='Chips',
        item_type='Ingredient'
    )

    return food_intake, food_intake_detail

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
