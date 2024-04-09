import pytest
from datetime import datetime, timedelta
from myapp.models import Profile, UserDaily, NutritionStats

@pytest.fixture
def create_user_daily(profile):
    def _create_user_daily(date, total_nutrients):
        return UserDaily.objects.create(profile=profile, date=date, total_nutrients=total_nutrients)
    return _create_user_daily

@pytest.fixture
def create_nutrition_stats(profile):
    def _create_nutrition_stats():
        return NutritionStats.objects.create(profile=profile)
    return _create_nutrition_stats

@pytest.mark.django_db
def test_compute_last_week_nutrients(create_user_daily, create_nutrition_stats):
    # Create a profile
    profile = Profile.objects.create(username="test_user")

    # Create UserDaily instances for the last week
    today = datetime.now().date()
    for i in range(7):
        date = today - timedelta(days=i)
        total_nutrients = {"Calories": 100, "Protein": 20, "Fat": 10}  # Example total nutrients for testing
        create_user_daily(date, total_nutrients)

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
