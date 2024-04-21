import pytest
from datetime import date
from django.utils.translation import gettext_lazy as _
from food_intake.food_intake import FoodIntake
from django.core.exceptions import ValidationError
import datetime

MEAL_TYPES = ['Breakfast', 'Lunch', 'Dinner', 'Snack']

@pytest.mark.django_db
@pytest.mark.parametrize('meal_type', MEAL_TYPES)
def test_food_intake_creation(user_profile, meal_type):
    intake_date = date.today()

    # Create a FoodIntake object
    food_intake = FoodIntake.objects.create(
        profile=user_profile,
        meal_type=meal_type,
        date=intake_date
    )

    # Check if the object is created successfully
    assert food_intake.pk is not None

    # Check if the attributes are set correctly
    assert food_intake.profile == user_profile
    assert food_intake.meal_type == meal_type
    assert food_intake.date == intake_date
    print(food_intake.meal_type)


@pytest.mark.xfail
@pytest.mark.django_db
def test_invalid_meal_type_validation(user_profile):
    invalid_meal_type = 'Invalid Meal Type'
    intake_date = date.today()

    # Attempt to create a FoodIntake object with an invalid meal type
    with pytest.raises(ValidationError) as e:
        FoodIntake.objects.create(
            profile=user_profile,
            meal_type=invalid_meal_type,
            date=intake_date
        )

    # Check if the expected validation error message is raised
    assert str(e.value) == f"'{invalid_meal_type}' is not a valid choice."


@pytest.mark.xfail
@pytest.mark.django_db
def test_invalid_date_validation(user_profile):
    invalid_date = datetime.date(2028, 1, 1)

    # Attempt to create a FoodIntake object with an invalid date
    with pytest.raises(ValidationError) as e:
        FoodIntake.objects.create(
            profile=user_profile,
            meal_type='Breakfast',  # Provide a valid meal type
            date=invalid_date
        )

    # Check if the expected validation error message is raised
    assert str(e.value) == 'Invalid date. Please provide a valid date.'
