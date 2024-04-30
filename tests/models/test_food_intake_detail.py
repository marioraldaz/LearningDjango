import pytest
from food_intake.models import FoodIntakeDetail


@pytest.fixture
def test_food_intake(food_intake_factory):
    # Create a test FoodIntake instance using the factory
    return food_intake_factory()

@pytest.fixture
def test_food_intake_detail(food_intake_detail_factory, test_food_intake):
    # Create a test FoodIntakeDetail instance associated with the test FoodIntake
    return food_intake_detail_factory(food_intake=test_food_intake)

@pytest.mark.django_db
def test_food_intake_detail_creation(food_intake_detail_factory, food_intake_factory):
    # Ensure the test FoodIntakeDetail instance is created and associated with the correct FoodIntake
    assert isinstance(food_intake_detail_factory, FoodIntakeDetail)
    assert food_intake_detail_factory.food_intake == food_intake_factory()

@pytest.mark.django_db
def test_food_intake_detail_nutrients_data(test_food_intake_detail):
    # Test get_nutrients_data method
    nutrients_data = test_food_intake_detail.get_nutrients_data()
    assert isinstance(nutrients_data, dict)

@pytest.mark.django_db
def test_food_intake_detail_properties_data(test_food_intake_detail):
    # Test get_properties_data method
    properties_data = test_food_intake_detail.get_properties_data()
    assert isinstance(properties_data, dict)

@pytest.mark.django_db
def test_food_intake_detail_flavonoids_data(test_food_intake_detail):
    # Test get_flavonoids_data method
    flavonoids_data = test_food_intake_detail.get_flavonoids_data()
    assert isinstance(flavonoids_data, dict)

@pytest.mark.django_db
def test_food_intake_detail_caloric_breakdown_data(test_food_intake_detail):
    # Test get_caloric_breakdown_data method
    caloric_breakdown_data = test_food_intake_detail.get_caloric_breakdown_data()
    assert isinstance(caloric_breakdown_data, dict)

@pytest.mark.django_db
def test_food_intake_detail_weight_per_serving_data(test_food_intake_detail):
    # Test get_weight_per_serving_data method
    weight_per_serving_data = test_food_intake_detail.get_weight_per_serving_data()
    assert isinstance(weight_per_serving_data, dict)
