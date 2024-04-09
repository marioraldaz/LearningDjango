import factory
from food_intake.food_intake import FoodIntake
from profiles.factories.profile_factory import ProfileFactory  

class FoodIntakeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = FoodIntake

    profile = factory.SubFactory(ProfileFactory)  # Create a related UserProfile instance
    meal_type = factory.Faker('random_element', elements=['Breakfast', 'Lunch', 'Dinner', 'Snack'])
    intake_date = factory.Faker('date_this_month')  # Generate a random date within the current month
