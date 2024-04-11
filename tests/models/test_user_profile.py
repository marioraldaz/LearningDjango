import pytest
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ValidationError
from datetime import datetime, date
from profiles.user_profile import UserProfile
from factories.profile_factory import UserProfileFactory

#Basic test using factory
@pytest.mark.django_db
def test_user_profile_factory():
    # Create a UserProfile instance using the factory
    UserProfileFactory(username='test_user', email='test@example.com', gender='Male', weight=70, height=180, date_of_birth='2000-01-01', activityLevel=1)

    # Verify that a UserProfile instance was created
    assert UserProfile.objects.count() == 1

    # Retrieve the created UserProfile instance
    user_profile = UserProfile.objects.get(username='test_user')
    print(user_profile)
    # Verify attributes of the UserProfile instance
    assert user_profile.email == 'test@example.com'
    assert user_profile.gender == 'Male'
    assert user_profile.weight == 70
    assert user_profile.height == 180
    assert user_profile.date_of_birth.strftime('%Y-%m-%d') == '2000-01-01'
    assert user_profile.activityLevel == 1

    # Test for non-existent username (optional)
    with pytest.raises(ObjectDoesNotExist):
        UserProfile.objects.get(username='non_existent_user')




#Test for all possible inputs

@pytest.mark.xfail
@pytest.mark.django_db
@pytest.mark.parametrize(
    "username, password, gender, email, weight, height, date_of_birth, profile_picture, activityLevel, expected_valid",
    [
        # Invalid username: shorter than 6 characters
        ("short", "valid_password", "Male", "valid@example.com", 80.0, 170.0, date(2000, 1, 1), None, 1, False),
        # Invalid password: shorter than 6 characters
        ("valid_username", "short", "Male", "valid@example.com", 80.0, 170.0, date(2000, 1, 1), None, 1, False),
        # Invalid email: incorrect format
        ("valid_username", "valid_password", "Male", "invalid_email", 80.0, 170.0, date(2000, 1, 1), None, 1, False),
        # Invalid weight: negative value
        ("valid_username", "valid_password", "Male", "valid@example.com", -5.0, 170.0, date(2000, 1, 1), None, 1, False),
        # Invalid height: negative value
        ("valid_username", "valid_password", "Male", "valid@example.com", 80.0, -170.0, date(2000, 1, 1), None, 1, False),
    ]
)
def test_user_profile_validation(username, password, gender, email, weight, height, date_of_birth, profile_picture, activityLevel, expected_valid):
    try:
        print(username, password, gender, email, weight, height, date_of_birth, profile_picture, activityLevel, expected_valid)
        # Use the factory to create a UserProfile object
        UserProfileFactory(
            username=username,
            password=password,
            gender=gender,
            email=email,
            weight=weight,
            height=height,
            date_of_birth=date_of_birth,
            activityLevel=activityLevel
        )
        
        # Retrieve the created UserProfile object from the database
        created_profile = UserProfile.objects.get(username=username)
        print(created_profile)

        assert expected_valid, f"Expected validation to fail for username={username}, password={password}, email={email}, weight={weight}, height={height}, date_of_birth={date_of_birth}, activityLevel={activityLevel}"
    except ValidationError as e:
        print(e)
        assert not expected_valid, f"Unexpected validation error: {e} for username={username}, password={password}, email={email}, weight={weight}, height={height}, date_of_birth={date_of_birth}, activityLevel={activityLevel}"
