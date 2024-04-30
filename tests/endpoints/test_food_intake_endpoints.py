import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from food_intake.models import FoodIntake
from profiles.user_profile import UserProfile
from django.utils import timezone

@pytest.fixture
def api_client():
    """Fixture for creating an instance of the Django test client."""
    return APIClient()

@pytest.fixture
def create_user_profile():
    def _create_user_profile():
        user_profile = UserProfile.objects.create(
            username='test_user',
            password='test_password',
            gender='Male',
            email='test@example.com',
            weight=80,
            height=170,
            date_of_birth='2000-01-01',
            activityLevel=1
        )
        return user_profile
    
    return _create_user_profile

@pytest.mark.django_db
def test_food_intake_post_no_client(api_client, create_user_profile):
    """Test the POST method of FoodIntakeView with missing 'profile_id'."""
    url = reverse('food_intake')
    
    # Create a new user profile for this test case
    user_profile = create_user_profile()
    
    # Create a request payload with the newly created user's ID as 'profile_id'
    data = {
        'profile_id': user_profile.id,
        'meal_type': 'Breakfast',
        'date': '2024-04-30',
        'details': [
            {
                'content_type': 'ingredient',
                'food_id': 1,
                'amount': 150
            }
        ]
    }
    
    # Send a POST request to the food_intake endpoint with the specified data
    response = api_client.post(url, data, format='json')
    
    # Assert the response status code is 400 (Bad Request)
    assert response.status_code == 400
    
    # Parse the response data as JSON to access error details
    response_data = response.json()
    
    # Get the list of error messages for the 'profile' field (should be required)
    profile_errors = response_data.get('profile', [])
    
    # Assert that there is at least one error message for the 'profile' field
    assert len(profile_errors) > 0
    assert 'This field is required.' in profile_errors

@pytest.mark.django_db
@pytest.mark.parametrize(
    'data, expected_status, expected_errors',
    [
        # Missing 'profile_id' field
        (
            {
                'meal_type': 'Breakfast',
                'date': '2024-04-30',
                'details': [
                    {
                        'content_type': 'ingredient',
                        'food_id': 1,
                        'amount': 150
                    }
                ]
            },
            status.HTTP_400_BAD_REQUEST,
            {'profile_id': ['This field is required.']}
        ),
        # Invalid date format
        (
            {
                'profile_id': 1,
                'meal_type': 'Breakfast',
                'date': '30-04-2024',  # Incorrect date format
                'details': [
                    {
                        'content_type': 'ingredient',
                        'food_id': 1,
                        'amount': 150
                    }
                ]
            },
            status.HTTP_400_BAD_REQUEST,
            {'date': ['Date has wrong format. Use YYYY-MM-DD format.']}
        ),
        # Missing 'details' field
        (
            {
                'profile_id': 1,
                'meal_type': 'Breakfast',
                'date': '2024-04-30'
            },
            status.HTTP_400_BAD_REQUEST,
            {'details': ['This field is required.']}
        ),
        # Invalid detail information
        (
            {
                'profile_id': 1,
                'meal_type': 'Breakfast',
                'date': '2024-04-30',
                'details': [
                    {
                        'content_type': '',  # Missing content_type
                        'food_id': 1,
                        'amount': 150
                    },
                    {
                        'content_type': 'ingredient',
                        'food_id': '',  # Missing food_id
                        'amount': 200
                    },
                    {
                        'content_type': 'recipe',
                        'food_id': 2,
                        'amount': -100  # Invalid amount (negative)
                    }
                ]
            },
            status.HTTP_400_BAD_REQUEST,
            {
                'details': [
                    {'content_type': ['This field may not be blank.']},
                    {'food_id': ['This field is required.']},
                    {'amount': ['Ensure this value is greater than 0.']}
                ]
            }
        ),
        # Add more test cases as needed
    ]
)
def test_food_intake_post_invalid(api_client, create_user_profile, data, expected_status, expected_errors):
    """Test the POST method of FoodIntakeView with different scenarios."""
    url = reverse('food_intake')

    # Create a new user profile for this test case
    user_profile = create_user_profile()

    # Update the 'profile_id' in the data dictionary with the new user's ID
    data['profile_id'] = user_profile.id

    # Send a POST request to the food_intake endpoint with the specified data
    response = api_client.post(url, data, format='json')

    # Assert the response status code matches the expected status
    assert response.status_code == expected_status

    # Parse the response data as JSON to access error details
    response_data = response.json()

    # Assert that the response data contains the expected error messages
    for field, expected_error in expected_errors.items():
        assert response_data.get(field) == expected_error

@pytest.mark.django_db
def test_successful_food_intake(api_client, create_user_profile, food_intake_detail_factory):
    """Test successful creation of FoodIntake records."""
    url = reverse('food_intake')

    # Create a new user profile for this test case
    user_profile = create_user_profile()

    # Create FoodIntakeDetail instances using the factory
    detail1 = food_intake_detail_factory(food_id=1, amount=300)
    detail2 = food_intake_detail_factory(food_id=2, amount=250)

    # Define the test data with FoodIntakeDetail instances
    data = {
        'profile_id': user_profile.id,
        'meal_type': 'Lunch',
        'date': '2024-05-01',
        'details': [
            {
                'content_type': 'recipe',
                'food_id': detail1.food_id,
                'amount': detail1.amount
            },
            {
                'content_type': 'recipe',
                'food_id': detail2.food_id,
                'amount': detail2.amount
            }
        ]
    }

    # Send a POST request to the food_intake endpoint with the specified data
    response = api_client.post(url, data, format='json')
    
    # Assert the response status code is 201 Created
    assert response.status_code == status.HTTP_201_CREATED, f"Failed to create FoodIntake: {response.data}"

    # Verify that the data is correctly saved in the database
    intake_id = response.data.get('id')
    assert intake_id is not None, "ID of created FoodIntake is missing in response data"

    # Retrieve the FoodIntake object from the database
    try:
        food_intake = FoodIntake.objects.get(id=intake_id)
    except FoodIntake.DoesNotExist:
        pytest.fail(f"FoodIntake object with id {intake_id} not found in the database.")

    # Verify that the retrieved object matches the input data
    assert food_intake.profile_id == data['profile_id'], "Profile ID does not match"
    assert food_intake.meal_type == data['meal_type'], "Meal type does not match"
    assert food_intake.date.strftime('%Y-%m-%d') == data['date'], "Date does not match"

    # Verify the details (foods) associated with the food intake
    expected_details = data['details']
    actual_details = food_intake.details.all()

    assert len(actual_details) == len(expected_details), "Number of details does not match"

    for i, expected_detail in enumerate(expected_details):
        actual_detail = actual_details[i]
        assert actual_detail.content_type.name == expected_detail['content_type'], f"Content type does not match for detail {i}"
        assert actual_detail.food_id == expected_detail['food_id'], f"Food ID does not match for detail {i}"
        assert actual_detail.amount == expected_detail['amount'], f"Amount does not match for detail {i}"