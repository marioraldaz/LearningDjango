from ...user_profile import UserProfile
import pytest

@pytest.fixture
@pytest.mark.django_db
def create_user_profile():
    user_profile = UserProfile.objects.create(
        username='test_user',
        password='test_password',
        gender='Male', 
        email='test@example.com',
        weight=70,
        height=180,
        date_of_birth='2000-01-01',
        activityLevel=1
    )
    yield user_profile
    user_profile.delete()  # Clean up after the test
    
@pytest.mark.django_db
def test_user_profile(create_user_profile):
    # Verify that a UserProfile instance was created
    assert UserProfile.objects.count() == 1

    # Retrieve the created UserProfile instance
    user_profile = UserProfile.objects.get(username='test_user')

    # Verify attributes of the UserProfile instance
    assert user_profile.email == 'test@example.com'
    assert user_profile.gender == 'Male'
    assert user_profile.weight == 70
    assert user_profile.height == 180
    assert user_profile.date_of_birth.strftime('%Y-%m-%d') == '2000-01-01'
    assert user_profile.activityLevel == 1

    # Test for non-existent username (optional)
    with pytest.raises(UserProfile.DoesNotExist):
        UserProfile.objects.get(username='non_existent_user')

    # Add more assertions as needed for other attributes or edge cases
