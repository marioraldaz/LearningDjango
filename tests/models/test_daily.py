import pytest
from django.core.exceptions import ValidationError
from datetime import datetime, date
from profiles.user_profile import UserProfile
from factories.user_profile_factory import UserProfileFactory

# Test for all possible inputs
@pytest.mark.django_db
@pytest.mark.parametrize(
    "username, gender, email, weight, height, date_of_birth, activityLevel, expected_valid",
    [
        # Invalid username: shorter than 6 characters
        ("short", "Male", "valid@example.com", 80.0, 170.0, date(2000, 1, 1), 1, False),
        # Invalid email: incorrect format
        ("valid_username", "Male", "invalid_email", 80.0, 170.0, date(2000, 1, 1), 1, False),
        # Invalid weight: negative value
        ("valid_username", "Male", "valid@example.com", -5.0, 170.0, date(2000, 1, 1), 1, False),
        # Invalid height: negative value
        ("valid_username", "Male", "valid@example.com", 80.0, -170.0, date(2000, 1, 1), 1, False),
    ]
)
def test_user_profile_validation(username, gender, email, weight, height, date_of_birth, activityLevel, expected_valid):
    try:
        # Use the factory to create a UserProfile object
        UserProfileFactory(
            username=username,
            gender=gender,
            email=email,
            weight=weight,
            height=height,
            date_of_birth=date_of_birth,
            activityLevel=activityLevel
        )
        # If the expected_valid is False, the test should fail if no ValidationError is raised
        assert expected_valid is False, f"Expected ValidationError for {username}"
    except ValidationError as e:
        # If the expected_valid is True, the test should fail if a ValidationError is raised
        assert expected_valid is True, f"Unexpected ValidationError: {e} for {username}"
