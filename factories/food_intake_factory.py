import factory
from food_intake.food_intake import FoodIntake
from factories.profile_factory import UserProfileFactory  

class FoodIntakeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = FoodIntake

    profile = factory.SubFactory(UserProfileFactory)  # Create a related UserProfile instance
    meal_type = factory.Faker('random_element', elements=['Breakfast', 'Lunch', 'Dinner', 'Snack'])
    intake_date = factory.Faker('date_this_month')  # Generate a random date within the current month
