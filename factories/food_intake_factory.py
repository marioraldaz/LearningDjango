import factory
from food_intake.food_intake import FoodIntake
from factories.user_profile_factory import UserProfileFactory  
from factories.user_daily_factory import UserDailyFactory
class FoodIntakeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = FoodIntake

    profile = factory.SubFactory(UserProfileFactory)
    meal_type = factory.Faker('random_element', elements=['Breakfast', 'Lunch', 'Dinner', 'Snack'])
    date = factory.Faker('date')
