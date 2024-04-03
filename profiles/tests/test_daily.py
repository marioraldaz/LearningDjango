import pytest
from django.core.exceptions import ValidationError
from django.utils import timezone
from ..user_daily import UserDaily

@pytest.mark.django_db
def test_daily_nutritional_stats_model(create_user_profile):
    # Test creating a valid DailyNutritionalStats record
    date = timezone.now().date()
    daily_stats = UserDaily.objects.create(
        profile=create_user_profile,
        date=date,
        total_calories_consumed=1500.0,
        total_protein_consumed=100.0,
        total_fat_consumed=50.0,
        total_carbohydrates_consumed=200.0
    )
    assert daily_stats.id is not None
    assert daily_stats.profile == create_user_profile  # Fix variable name here
    assert daily_stats.date == date
    assert daily_stats.total_calories_consumed == 1500.0
    assert daily_stats.total_protein_consumed == 100.0
    assert daily_stats.total_fat_consumed == 50.0
    assert daily_stats.total_carbohydrates_consumed == 200.0

    # Test creating a DailyNutritionalStats record with negative total calories consumed
    with pytest.raises(ValidationError):
        UserDaily.objects.create(
            profile=create_user_profile,
            date=date,
            total_calories_consumed=-500.0,
            total_protein_consumed=100.0,
            total_fat_consumed=50.0,
            total_carbohydrates_consumed=200.0
        )

    # Test creating a DailyNutritionalStats record with invalid date format
    with pytest.raises(ValidationError):
        UserDaily.objects.create(
            profile=create_user_profile,
            date='invalid_date',
            total_calories_consumed=1500.0,
            total_protein_consumed=100.0,
            total_fat_consumed=50.0,
            total_carbohydrates_consumed=200.0
        )
