import pytest
from django.core.exceptions import ValidationError
from ..factories.user_daily_factory import UserDailyFactory
from datetime import datetime 

@pytest.mark.django_db
@pytest.mark.parametrize(
    "total_calories_consumed, total_protein_consumed, total_fat_consumed, total_carbohydrates_consumed, expected_exception",
    [
        (1500.0, 100.0, 50.0, 200.0, None),  # Valid data, no exception expected
        (-500, 100.0, 50.0, 200.0, ValidationError),  # Negative calories, expect ValidationError
        (2000.0, -50.0, 50.0, 200.0, ValidationError),  # Negative protein, expect ValidationError
        (2500.0, 150.0, -25.0, 200.0, ValidationError),  # Negative fat, expect ValidationError
        (3000.0, 200.0, 75.0, -100.0, ValidationError),  # Negative carbohydrates, expect ValidationError
        (3500.0, 300.0, 100.0, 300.0, None),  # Upper limit for each nutrient, no exception expected
    ],
)
def test_user_daily_factory(total_calories_consumed, total_protein_consumed, total_fat_consumed, total_carbohydrates_consumed, expected_exception):
    if expected_exception is not None:
        with pytest.raises(expected_exception):
            UserDailyFactory(
                total_calories_consumed=total_calories_consumed,
                total_protein_consumed=total_protein_consumed,
                total_fat_consumed=total_fat_consumed,
                total_carbohydrates_consumed=total_carbohydrates_consumed,
            )
    else:
        # If no exception is expected, create the UserDaily instance and assert its attributes
        daily_stats = UserDailyFactory(
            total_calories_consumed=total_calories_consumed,
            total_protein_consumed=total_protein_consumed,
            total_fat_consumed=total_fat_consumed,
            total_carbohydrates_consumed=total_carbohydrates_consumed,
        )
        assert daily_stats.id is not None
        assert daily_stats.total_calories_consumed == total_calories_consumed
        assert daily_stats.total_protein_consumed
