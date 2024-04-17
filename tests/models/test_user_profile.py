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
        ("valid_username", "Male", "valid@example.com", -5
