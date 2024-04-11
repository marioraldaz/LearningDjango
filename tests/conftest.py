import pytest
from pytest_factoryboy import register
from django.urls import reverse
from food_intake.food_intake import FoodIntake
from food_intake.food_intake_detail import FoodIntakeDetail
from factories.user_profile_factory import UserProfileFactory
from factories.food_intake_factory import FoodIntakeFactory
from factories.food_intake_detail_factory import FoodIntakeDetailFactory
from factories.ingredient_factory import IngredientFactory
from factories.nutrition_factory import NutritionFactory
from factories.nutrition_stats_factory import NutritionStatsFactory
from factories.recipe_factory import RecipeFactory
from factories.user_daily_factory import UserDailyFactory

register(UserProfileFactory, name="user_profile_factory")
register(FoodIntakeFactory, name="food_intake_factory")
register(FoodIntakeDetailFactory, name="food_intake_detail_factory")
register(IngredientFactory, name="ingredient_factory")
register(NutritionFactory, name="nutrition_factory")
register(NutritionStatsFactory, name="nutrition_stats_factory")
register(RecipeFactory, name="recipe_factory")
register(UserDailyFactory, name="user_daily_factory")

@pytest.fixture
def create_user_profile():
    user_profile=UserProfileFactory.create()
    return user_profile
    

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