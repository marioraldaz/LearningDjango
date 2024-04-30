import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from food_intake.models import UserDaily, FoodIntake, FoodIntakeDetail

@pytest.fixture
def api_client():
    """Fixture for creating an instance of the Django test client."""
    return APIClient()

@pytest.mark.django_db
def test_get_user_dailies(api_client, user_daily_factory):
    """Test GET request to retrieve user dailies by profile ID."""
    profile_id = 1
    user_daily = user_daily_factory.create()
    
    user_daily.profile_id = profile_id
    
        # Retrieve all UserDaily objects
    user_dailies = UserDaily.objects.all()

    # Iterate through each UserDaily object in the queryset
    for user_daily in user_dailies:
        # Print the attributes and values for the current UserDaily object
        for attr, value in user_daily.__dict__.items():
            print(f"{attr}: {value}")
        print()  # Print a blank line to separate different objects
    
    url = reverse('user_dailies', kwargs={'profile_id': profile_id})
    
    response = api_client.get(url)
    
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1  # Assuming we expect one user daily entry
    # Add more assertions based on expected response data



@pytest.mark.django_db
def test_user_daily_view_post(api_client, user_profile_factory):
    """Test POST request to UserDailyView to create a new user daily entry."""
    user_profile_factory.create(id=1)
    
    url = reverse('user_dailies', kwargs={'profile_id': 1})
    
    
    data = {
        'date': '2024-05-01',  
        'profile': 1,  
        'total_nutrients': {}, 
        'total_properties': {},
        'total_flavonoids': {},
        'total_caloric_breakdown': {},
        'total_weight_per_serving': {}
    }
    
    response = api_client.post(url, data, format='json')
    
    assert response.status_code == status.HTTP_201_CREATED
    assert UserDaily.objects.filter(profile_id=1).exists()  # Check if the user daily entry was created
    # Add more assertions to validate the response and the created user daily entry
    
@pytest.mark.xfail
@pytest.mark.django_db
def test_user_daily_view_list_food_intakes_with_details(api_client, food_intake_factory, food_intake_detail_factory, user_profile_factory):
    """Test GET request to UserDailyView to retrieve food intakes with details."""
    # Create sample food intake with details for testing
    user_profile_factory.create(id=1)
    food_intake = food_intake_factory(profile_id=1)
    food_intake_detail_factory(food_intake=food_intake)
    
    url = reverse('list_food_intakes_with_details')
    
    response = api_client.get(url)
    
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1  # Assuming we expect one food intake with details
    
    # Validate the response data structure
    intake_data = response.data[0]
    assert 'food_intake' in intake_data
    assert 'details' in intake_data
    
    # Validate the food intake data
    food_intake_data = intake_data['food_intake']
    assert food_intake_data['id'] == food_intake.id
    # Add more assertions based on expected food intake fields
    
    # Validate the intake details data
    details_data = intake_data['details']
    assert len(details_data) == 1  # Assuming one detail entry for the food intake
    # Add more assertions based on expected detail fields
    
    # Optionally, assert on specific values within the food intake and details data