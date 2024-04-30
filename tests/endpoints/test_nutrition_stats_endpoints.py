import pytest
from django.urls import reverse
from food_intake.models import NutritionStats
from rest_framework.test import APIClient
from rest_framework import status
from django.utils import timezone
from datetime import timedelta
from food_intake.models import NutritionStats, UserDaily

@pytest.fixture
def api_client():
    # Return Django REST Framework's APIClient
    return APIClient()

@pytest.fixture
def sample_nutrition_stats(user_profile_factory, user_daily_factory):
    # Create a sample UserProfile and associated NutritionStats instance
    profile = user_profile_factory()
    return NutritionStats.objects.create(profile=profile)


@pytest.mark.django_db
def test_nutrition_stats_detail_view(api_client, nutrition_stats_factory):
    # Create a NutritionStats instance using the factory
    nutrition_stats = nutrition_stats_factory()

    # Generate the URL for the NutritionStatsDetailView using the profile ID
    url = reverse('nutrition_stats_detail', kwargs={'profile_id': nutrition_stats.profile.id})

    # Use the Django REST Framework's APIClient to perform a GET request to the view
    response = api_client.get(url)

    # Assert that the view returns a successful response (status code 200)
    assert response.status_code == status.HTTP_200_OK

    # Check individual fields in the response data
    assert response.data['id'] == nutrition_stats.id
    assert response.data['profile'] == nutrition_stats.profile.id
    assert response.data['last_week_calories'] == nutrition_stats.last_week_calories
    assert response.data['last_week_fat'] == nutrition_stats.last_week_fat
    assert response.data['last_week_saturated_fat'] == nutrition_stats.last_week_saturated_fat
 
        
        
@pytest.mark.django_db
def test_nutrition_stats_id(api_client, nutrition_stats_factory):
    nutrition_stats = nutrition_stats_factory()
    url = reverse('nutrition_stats_detail', kwargs={'profile_id': nutrition_stats.profile.id})
    response = api_client.get(url)
    assert response.data['id'] == nutrition_stats.id

@pytest.mark.django_db
def test_nutrition_stats_profile(api_client, nutrition_stats_factory):
    nutrition_stats = nutrition_stats_factory()
    url = reverse('nutrition_stats_detail', kwargs={'profile_id': nutrition_stats.profile.id})
    response = api_client.get(url)
    assert response.data['profile'] == nutrition_stats.profile.id


@pytest.fixture
def create_user_dailies_for_period(sample_nutrition_stats, user_daily_factory):
    def _create_user_dailies(period_days):
        today = timezone.now().date()
        user_dailies = []

        for i in range(period_days):
            date = today - timedelta(days=i)
            user_daily = user_daily_factory(profile=sample_nutrition_stats.profile, date=date)
            user_dailies.append(user_daily)

        return user_dailies

    return _create_user_dailies

@pytest.mark.django_db
@pytest.mark.parametrize('period_days', [7, 30])
def test_compute_nutrients_period(sample_nutrition_stats, create_user_dailies_for_period, period_days):
    # Create UserDaily instances for the specified period
    user_dailies = create_user_dailies_for_period(period_days)

    # Call the appropriate compute method based on the period
    if period_days == 7:
        sample_nutrition_stats.compute_last_week_nutrients()
    elif period_days == 30:
        sample_nutrition_stats.compute_last_30_days_nutrients()

    # Retrieve the updated NutritionStats instance from the database
    updated_stats = NutritionStats.objects.get(id=sample_nutrition_stats.id)

    # Debugging output
    print("Updated NutritionStats:", updated_stats)
    expected_calories_sum = sum(user_daily.total_nutrients.get('Calories', 0) for user_daily in user_dailies)
    print(f"Expected Calories Sum ({period_days} days):", expected_calories_sum)

    # Verify that nutrient fields are updated correctly for the specified period
    if period_days == 7:
        assert updated_stats.last_week_calories is not None
        assert updated_stats.last_week_calories == expected_calories_sum
    elif period_days == 30:
        assert updated_stats.last_30_days_calories is not None
        assert updated_stats.last_30_days_calories == expected_calories_sum