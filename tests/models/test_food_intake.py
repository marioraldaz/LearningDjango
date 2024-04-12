import pytest
from django.core.exceptions import ValidationError
from food_intake.food_intake import FoodIntake

# Test case for creating a food intake instance
@pytest.mark.django_db
def test_create_food_intake(user_profile_factory, user_daily_factory, food_intake_factory):
    user_profile = user_profile_factory.create()  # Create UserProfile instance
    user_daily = user_daily_factory.create()  # Create UserDaily instance
    food_intake = food_intake_factory.create(profile=user_profile, user_daily=user_daily)
    assert food_intake.profile == user_profile
    assert food_intake.user_daily == user_daily
    

# Test case to ensure meal type choices are limited to specified options
@pytest.mark.django_db
def test_meal_type_choices(user_profile_factory, user_daily_factory):
    user_profile = user_profile_factory.create()  # Create UserProfile instance
    user_daily = user_daily_factory.create()  # Create UserDaily instance
    
  
    # Attempt to create and save the FoodIntake object with an invalid meal_type
    food = FoodIntake(
        profile=user_profile,
        user_daily=user_daily,
        meal_type="Invalid"
    )
    food.save()
    with pytest.raises(ValidationError): # ASssert the validation error
        food.full_clean()
    
  
# Test case to check the relationship between FoodIntake and UserProfile
@pytest.mark.django_db
def test_food_intake_user_profile_relationship(user_profile_factory, user_daily_factory, food_intake_factory):
    user_profile = user_profile_factory.create()  # Create UserProfile instance
    user_daily = user_daily_factory.create()  # Create UserDaily instance
    food_intake = food_intake_factory.create(profile=user_profile, user_daily=user_daily)
    assert food_intake.profile == user_profile

# Test case to check the relationship between FoodIntake and UserDaily
@pytest.mark.django_db
def test_food_intake_user_daily_relationship(user_profile_factory, user_daily_factory, food_intake_factory):
    user_profile = user_profile_factory.create()  # Create UserProfile instance
    user_daily = user_daily_factory.create()  # Create UserDaily instance
    food_intake = food_intake_factory.create(profile=user_profile, user_daily=user_daily)
    assert food_intake.user_daily == user_daily


