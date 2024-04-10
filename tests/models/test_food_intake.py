import pytest
from django.urls import reverse
from food_intake.food_intake import FoodIntake
from food_intake.tests.factories.food_intake_factory import FoodIntakeFactory
from profiles.tests.factories.profile_factory import ProfileFactory
from django.db import transaction
from django.db.transaction import TransactionManagementError

VALID_STATUS_CODE = 200
INVALID_STATUS_CODE = 400
NOT_FOUND_STATUS_CODE = 404
VALID_MEAL_TYPES = ['Breakfast', 'Lunch', 'Dinner', 'Snack']



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

    # Ensure the  contains the expected keys and values
    response_data = response.json()
    assert 'id' in response_data
    assert 'food_intake' in response_data
    assert 'item_name' in response_data
    assert 'item_type' in response_data

    # Assert on specific values if needed
    assert response_data['item_name'] == 'Chips'  # Assuming 'Chips' is the expected value
    assert response_data['item_type'] == 'Ingredient'  # Assuming 'Ingredient' is the expected value
"""

@pytest.fixture
def user_profile():
    return ProfileFactory()

@pytest.mark.django_db
@pytest.mark.parametrize(
    "meal_type, intake_date, expected_status_code, should_exist, error_message",
    [
        # Valid cases
        ('Breakfast', '2024-01-01', VALID_STATUS_CODE, True, None),
        ('Lunch', '2024-01-01', VALID_STATUS_CODE, True, None),
        ('Dinner', '2024-01-01', VALID_STATUS_CODE, True, None),
        ('Snack', '2024-01-01', VALID_STATUS_CODE, True, None),
        # Invalid cases
        ('Breakfast', '2024-01-01', INVALID_STATUS_CODE, False, "Duplicate meal type should return 400"),
        ('Breakfast', '2023-01-01', INVALID_STATUS_CODE, False, "Past date should return 400"),
        ('Breakfast', '2024-01-01', INVALID_STATUS_CODE, False, "Non-existing profile should return 404"),
    ]
)
def test_save_food_intake(client, meal_type, intake_date, expected_status_code, should_exist, error_message):
    try:
        with transaction.atomic():
            user_profile = None
            if should_exist:
                user_profile = ProfileFactory()

            url = reverse('save_food_intake')
            data = {'meal_type': meal_type, 'intake_date': intake_date}

            if user_profile:
                data['profile_id'] = user_profile.pk

            response = client.post(url, data)

            assert response.status_code == expected_status_code, f"Unexpected status code: {response.status_code}. {error_message}"

            # Check if the food intake was saved only when expected
            if should_exist:
                assert FoodIntake.objects.filter(meal_type=meal_type).exists(), f"Food intake for meal type {meal_type} should exist"
            else:
                assert not FoodIntake.objects.filter(meal_type=meal_type).exists(), f"Food intake for meal type {meal_type} should not exist"
    except TransactionManagementError as e:
        if should_exist:
            pytest.fail(f"TransactionManagementError occurred: {e}")


@pytest.mark.django_db
def test_food_intake_creation():
    intake = FoodIntakeFactory()
    assert FoodIntake.objects.count() == 1
    assert intake.profile is not None