from ..user_profile import UserProfile

def test_user_profile(create_user_profile):
    # The create_user_profile fixture is automatically invoked to set up test data
    assert UserProfile.objects.count() == 1
    user_profile = UserProfile.objects.get(username='test_user')
    assert user_profile.email == 'test@example.com'