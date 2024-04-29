from food_intake import user_daily
import pytest
from datetime import datetime, timedelta
from food_intake.nutrition_stats import NutritionStats
from django.utils import timezone

@pytest.fixture
def setup_user_daily_records(nutrition_stats_factory, user_daily_factory):
    # Create NutritionStats instance with associated UserProfile using the factory
    nutrition_stats = nutrition_stats_factory()

    today = timezone.now().date()
    last_week_start = today - timedelta(days=7)
    last_30_days_start = today - timedelta(days=30)

    # Create user daily records for the last week
    for day in range(7):
        date = last_week_start + timedelta(days=day)
        # Use nutrition_stats.profile to get the associated UserProfile
        user_daily_factory(profile=nutrition_stats.profile, date=date)

    # Create user daily records for the last 30 days
    for day in range(30):
        date = last_30_days_start + timedelta(days=day)
        # Use nutrition_stats.profile to get the associated UserProfile
        user_daily_factory(profile=nutrition_stats.profile, date=date)

@pytest.mark.django_db
def test_compute_last_week_nutrients(setup_user_daily_records, nutrition_stats_factory):
    # Call the factory method to create NutritionStats and set up related data
    nutrition_stats = nutrition_stats_factory()

    # Call the method to compute last week's nutrients
    nutrition_stats.compute_last_week_nutrients()

    # Retrieve the updated nutrition stats from the database
    updated_stats = NutritionStats.objects.get(id=nutrition_stats.id)

    # Assert that the last week's nutrient fields are updated
    assert updated_stats.last_week_calories is not None
    assert updated_stats.last_week_fat is not None
    # Add assertions for other nutrient fields

@pytest.mark.django_db
def test_compute_last_30_days_nutrients(setup_user_daily_records, nutrition_stats_factory):
    # Call the factory method to create NutritionStats and set up related data
    nutrition_stats = nutrition_stats_factory()

    # Call the method to compute last 30 days' nutrients
    nutrition_stats.compute_last_30_days_nutrients()

    # Retrieve the updated nutrition stats from the database
    updated_stats = NutritionStats.objects.get(id=nutrition_stats.id)

    # Assert that the last 30 days' nutrient fields are updated
    assert updated_stats.last_30_days_calories is not None
    assert updated_stats.last_30_days_fat is not None
    # Add assertions for other nutrient fields
