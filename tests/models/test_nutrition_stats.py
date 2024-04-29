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

    # Ensure that the computed values are non-negative
    assert updated_stats.last_week_calories >= 0
    assert updated_stats.last_week_fat >= 0
    # Add assertions for other nutrient fields

    # Test when no user dailies exist for the last week
    NutritionStats.objects.all().delete()  # Clear existing NutritionStats
    nutrition_stats.compute_last_week_nutrients()  # Recompute with no data
    updated_stats = NutritionStats.objects.get(id=nutrition_stats.id)
    assert updated_stats.last_week_calories == 0.0
    assert updated_stats.last_week_fat == 0.0
    # Add assertions for other nutrient fields

@pytest.mark.django_db
def test_compute_last_30_days_nutrients(setup_user_daily_records, nutrition_stats_factory, user_daily_factory):
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

    # Ensure that the computed values are non-negative
    assert updated_stats.last_30_days_calories >= 0
    assert updated_stats.last_30_days_fat >= 0
    # Add assertions for other nutrient fields

    # Test when no user dailies exist for the last 30 days
    NutritionStats.objects.all().delete()  # Clear existing NutritionStats
    nutrition_stats.compute_last_30_days_nutrients()  # Recompute with no data
    updated_stats = NutritionStats.objects.get(id=nutrition_stats.id)
    assert updated_stats.last_30_days_calories == 0.0
    assert updated_stats.last_30_days_fat == 0.0
    # Add assertions for other nutrient fields

    # Test scenario with only one day's data in the last 30 days
    NutritionStats.objects.all().delete()  # Clear existing NutritionStats
    today = timezone.now().date()
    user_daily_factory(profile=nutrition_stats.profile, date=today - timedelta(days=29))
    nutrition_stats.compute_last_30_days_nutrients()
    updated_stats = NutritionStats.objects.get(id=nutrition_stats.id)
    assert updated_stats.last_30_days_calories is not None
    assert updated_stats.last_30_days_fat is not None
    # Add assertions for other nutrient fields
    

@pytest.mark.django_db
def test_compute_nutrients(setup_user_daily_records, nutrition_stats_factory):
    # Call the factory method to create NutritionStats and set up related data
    nutrition_stats = nutrition_stats_factory()

    # Compute last week's nutrients
    nutrition_stats.compute_last_week_nutrients()

    # Retrieve the updated nutrition stats from the database
    updated_stats = NutritionStats.objects.get(id=nutrition_stats.id)

    # Assert that all last week's nutrient fields are updated and non-negative
    assert updated_stats.last_week_calories >= 0.0
    assert updated_stats.last_week_fat >= 0.0
    assert updated_stats.last_week_saturated_fat >= 0.0
    assert updated_stats.last_week_carbohydrates >= 0.0
    assert updated_stats.last_week_sugar >= 0.0
    assert updated_stats.last_week_protein >= 0.0
    assert updated_stats.last_week_cholesterol >= 0.0
    assert updated_stats.last_week_sodium >= 0.0
    assert updated_stats.last_week_fiber >= 0.0
    assert updated_stats.last_week_vitamin_c >= 0.0
    assert updated_stats.last_week_manganese >= 0.0
    assert updated_stats.last_week_folate >= 0.0
    assert updated_stats.last_week_potassium >= 0.0
    assert updated_stats.last_week_magnesium >= 0.0
    assert updated_stats.last_week_vitamin_a >= 0.0
    assert updated_stats.last_week_vitamin_b6 >= 0.0
    assert updated_stats.last_week_vitamin_b12 >= 0.0
    assert updated_stats.last_week_vitamin_d >= 0.0
    assert updated_stats.last_week_calcium >= 0.0
    assert updated_stats.last_week_iron >= 0.0
    assert updated_stats.last_week_zinc >= 0.0
    assert updated_stats.last_week_vitamin_e >= 0.0
    assert updated_stats.last_week_vitamin_k >= 0.0
    assert updated_stats.last_week_omega_3 >= 0.0
    assert updated_stats.last_week_omega_6 >= 0.0

    # Compute last 30 days' nutrients
    nutrition_stats.compute_last_30_days_nutrients()

    # Retrieve the updated nutrition stats from the database
    updated_stats = NutritionStats.objects.get(id=nutrition_stats.id)

    # Assert that all last 30 days' nutrient fields are updated and non-negative
    assert updated_stats.last_30_days_calories >= 0.0
    assert updated_stats.last_30_days_fat >= 0.0
    assert updated_stats.last_30_days_saturated_fat >= 0.0
    assert updated_stats.last_30_days_carbohydrates >= 0.0
    assert updated_stats.last_30_days_sugar >= 0.0
    assert updated_stats.last_30_days_protein >= 0.0
    assert updated_stats.last_30_days_cholesterol >= 0.0
    assert updated_stats.last_30_days_sodium >= 0.0
    assert updated_stats.last_30_days_fiber >= 0.0
    assert updated_stats.last_30_days_vitamin_c >= 0.0
    assert updated_stats.last_30_days_manganese >= 0.0
    assert updated_stats.last_30_days_folate >= 0.0
    assert updated_stats.last_30_days_potassium >= 0.0
    assert updated_stats.last_30_days_magnesium >= 0.0
    assert updated_stats.last_30_days_vitamin_a >= 0.0
    assert updated_stats.last_30_days_vitamin_b6 >= 0.0
    assert updated_stats.last_30_days_vitamin_b12 >= 0.0
    assert updated_stats.last_30_days_vitamin_d >= 0.0
    assert updated_stats.last_30_days_calcium >= 0.0
    assert updated_stats.last_30_days_iron >= 0.0
    assert updated_stats.last_30_days_zinc >= 0.0
    assert updated_stats.last_30_days_vitamin_e >= 0.0
    assert updated_stats.last_30_days_vitamin_k >= 0.0
    assert updated_stats.last_30_days_omega_3 >= 0.0
    assert updated_stats.last_30_days_omega_6 >= 0.0
