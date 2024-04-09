import pytest
from django.urls import reverse
from food_intake.food_intake import FoodIntake
from food_intake.food_intake_detail import FoodIntakeDetail
from profiles.user_profile import UserProfile

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