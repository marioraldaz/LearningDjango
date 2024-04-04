import pytest
from django.core.exceptions import ValidationError
from ...factories.user_daily_factory import UserDailyFactory, UserDailyNegativeValuesFactory
from datetime import date 
from ...user_profile import UserProfile
from ...user_daily import UserDaily
from ...factories.profile_factory import ProfileFactory  # Import your ProfileFactory
from ...utils.validators import validate_positive_float  # Import the validator function


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
def test_user_daily_edge_cases(total_calories_consumed, total_protein_consumed, total_fat_consumed, total_carbohydrates_consumed, expected_exception):
    
    # Call clean_fields() to trigger validation checks
    print(expected_exception)
    if expected_exception is not None:
        with pytest.raises(expected_exception):
            daily_stats = UserDaily.objects.create(
                profile=ProfileFactory(),  # Use ProfileFactory to create a test UserProfile instance
                date=date.today(),  # Use today's date
                total_calories_consumed=total_calories_consumed,
                total_protein_consumed=total_protein_consumed,
                total_fat_consumed=total_fat_consumed,
                total_carbohydrates_consumed=total_carbohydrates_consumed,
            )
            daily_stats.full_clean()  # Trigger validation explicitly
    else:
        # If no exception is expected, create the UserDaily instance and assert its attributes
        daily_stats = UserDaily.objects.create(
            profile=ProfileFactory(),  # Use ProfileFactory to create a test UserProfile instance
            date=date.today(),  # Use today's date
            total_calories_consumed=total_calories_consumed,
            total_protein_consumed=total_protein_consumed,
            total_fat_consumed=total_fat_consumed,
            total_carbohydrates_consumed=total_carbohydrates_consumed,
        )
        daily_stats.full_clean()  # Trigger validation explicitly

        
        # Assert the attributes of the created UserDaily instance
        assert daily_stats.id is not None
        assert daily_stats.total_calories_consumed == total_calories_consumed
        assert daily_stats.total_protein_consumed == total_protein_consumed
        assert daily_stats.total_fat_consumed == total_fat_consumed
        assert daily_stats.total_carbohydrates_consumed == total_carbohydrates_consumed
        
@pytest.mark.django_db
def test_random_user_daily_factory():
    num_instances = 10  # Number of random instances to create
    for _ in range(num_instances):
        daily_stats = UserDailyFactory()
        daily_stats.full_clean()  # Trigger validation explicitly
        # Assert that the instance was created successfully
        assert daily_stats.id is not None
        
@pytest.mark.django_db
def test_user_daily_simpleCreation():
    # Create a UserDaily instance using the factory
    daily_stats = UserDailyFactory.create(
        total_calories_consumed=1500.0,
        total_protein_consumed=100.0,
        total_fat_consumed=50.0,
        total_carbohydrates_consumed=200.0,
    )
    daily_stats.full_clean()  # Trigger validation explicitly
    # Assert the attributes of the created UserDaily instance
    assert daily_stats.id is not None
    assert daily_stats.total_calories_consumed == 1500.0
    assert daily_stats.total_protein_consumed == 100.0
    assert daily_stats.total_fat_consumed == 50.0
    assert daily_stats.total_carbohydrates_consumed == 200.0


@pytest.mark.django_db
def test_user_daily_simpleCreationWithFailure():
    # Use pytest.raises to check if a ValidationError is raised
    with pytest.raises(ValidationError) as e:
        # Create a UserDaily instance with a negative number using the factory
        daily_stats = UserDailyFactory.create(
            total_calories_consumed=-500.0,  # Negative value should raise ValidationError
            total_protein_consumed=100.0,
            total_fat_consumed=50.0,
            total_carbohydrates_consumed=200.0,
        )
        daily_stats.full_clean()  # Trigger validation explicitly
        
    error_dict = e.value.message_dict
    assert 'total_calories_consumed' in error_dict
    print(f"Error message: {error_dict['total_calories_consumed']}")
    assert 'Value must be a positive float or integer' in error_dict['total_calories_consumed']
    assert 'Ensure this value is greater than or equal to 0.' in error_dict['total_calories_consumed']
    print(f"Exception message: {str(e.value)}")

    # Ensure that the UserDaily instance was not created
    assert UserDaily.objects.exists()
    
@pytest.mark.django_db
def test_negative_values_validation():
    with pytest.raises(ValidationError):
        daily_stats = UserDailyFactory.create(
            total_calories_consumed=-500,
            total_protein_consumed=-100,
            total_fat_consumed=-50,
            total_carbohydrates_consumed=-200,
        )
        daily_stats.full_clean()  # Trigger validation explicitly