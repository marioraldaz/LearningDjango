from food_intake import user_daily
import pytest
from datetime import datetime, timedelta
from food_intake.nutrition_stats import NutritionStats
from factories.profile_factory import ProfileFactory
from factories.user_daily_factory import UserDailyFactory

@pytest.fixture
def profile(create_user_profile):
    return create_user_profile


@pytest.fixture
def create_user_daily():
    return UserDailyFactory.create()

@pytest.fixture
def create_nutrition_stats(profile):
    def _create_nutrition_stats():
        return NutritionStatsFactory.objects.create(profile=profile)
    return _create_nutrition_stats

@pytest.mark.django_db
def test_compute_last_week_nutrients(create_user_daily, create_nutrition_stats):
    
    # Create UserDaily instances for the last week
    today = datetime.now().date()
    for i in range(7):
        date = today - timedelta(days=i)
        total_nutrients = {"Calories": 100, "Protein": 20, "Fat": 10}  # Example total nutrients for testing
        user_daily = create_user_daily()
        user_daily.date = date
        user_daily.total_nutrients = total_nutrients
    # Create a NutritionStats instance
    nutrition_stats = create_nutrition_stats()

    # Call the method to compute last week nutrients
    nutrition_stats.compute_last_week_nutrients()

    # Retrieve the NutritionStats instance again to check the computed values
    nutrition_stats.refresh_from_db()

    # Assertions for last week nutrient totals
    assert nutrition_stats.last_week_calories == 700
    assert nutrition_stats.last_week_protein == 140
    assert nutrition_stats.last_week_fat == 70

# Similar tests for compute_last_30_days_nutrients, and other scenarios as needed...
