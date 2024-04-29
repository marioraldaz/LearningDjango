import pytest


# Test data with various scenarios
test_data = [
    # Valid scenarios
    ('Lose', 60, 60, 150, 1),  # Lose weight with sedentary activity level
    ('Maintain', 50, 70, 200, 3),  # Maintain weight with moderate activity level
    ('Gain', 70, 80, 250, 5),  # Gain weight with super active activity level

    # Invalid scenarios
    ('Lose', -10, 60, 150, 2),  # Invalid protein (negative value) with lightly active
    ('Maintain', 50, 1000, 200, 4),  # Invalid fat (exceeds max value) with very active
    ('Gain', 70, 80, -100, 1),  # Invalid carbohydrate (negative value) with sedentary
    ('Lose', 60, 60, 10000, 3),  # Invalid carbohydrate (exceeds max value) with moderate
    ('Maintain', 0, 70, 200, 5),  # Invalid protein (zero value) with super active
    ('Maintain', 50, -20, 200, 2),  # Invalid fat (negative value) with lightly active
    ('Gain', 70, 80, 0, 4),  # Invalid carbohydrate (zero value) with very active
    ('Lose', 60, 60, 150, 1),   # Valid scenario (boundary) with sedentary
    ('Gain', 500, 500, 1000, 5),  # Valid scenario (boundary) with super active
    ('Maintain', 499, 499, 999, 4),  # Valid scenario (boundary) with very active
    ('Lose', 0, 0, 0, 3),   # Invalid (all values zero) with moderate
]

@pytest.mark.django_db
@pytest.mark.parametrize("goal, protein, fat, carbohydrate, activity_level", test_data)
def test_user_fitness_profile_creation(user_fitness_profile_factory, goal, protein, fat, carbohydrate, activity_level):
    # Create a UserFitnessProfile instance using the factory with specified parameters
    user_fitness_profile = user_fitness_profile_factory(
        goal=goal,
        daily_protein_goal=protein,
        daily_fat_goal=fat,
        daily_carbohydrate_goal=carbohydrate,
        activity_level=activity_level
    )

    # Validate the UserFitnessProfile instance
    assert user_fitness_profile is not None
    assert user_fitness_profile.goal == goal
    assert user_fitness_profile.daily_protein_goal == protein
    assert user_fitness_profile.daily_fat_goal == fat
    assert user_fitness_profile.daily_carbohydrate_goal == carbohydrate
    assert user_fitness_profile.activity_level == activity_level

        
        
@pytest.mark.django_db
def test_user_fitness_profile_goal(user_fitness_profile):
    # Test specific behavior related to the goal attribute
    assert user_fitness_profile.goal != ''
    assert user_fitness_profile.goal in ['Lose', 'Maintain', 'Gain']
    
@pytest.mark.django_db
def test_user_fitness_profile_activity_level(user_fitness_profile):
    # Test specific behavior related to the activity_level attribute
    assert user_fitness_profile.activity_level >= 1
    assert user_fitness_profile.activity_level <= 5