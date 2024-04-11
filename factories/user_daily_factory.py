import factory
from django.utils import timezone
from faker import Faker  # Import Faker
from food_intake.user_daily import UserDaily
from profiles.user_profile import UserProfile
from factories.user_profile_factory import UserProfileFactory
fake = Faker()  # Initialize Faker
    
class UserDailyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserDaily

    date = factory.Faker('date')
    total_nutrients = factory.Faker('pydict', value_types=['float'], nb_elements=5)
    total_properties = factory.Faker('pydict', value_types=['float'], nb_elements=5)
    total_flavonoids = factory.Faker('pydict', value_types=['float'], nb_elements=5)
    total_caloric_breakdown = factory.Faker('pydict', value_types=['float'], nb_elements=5)
    total_weight_per_serving = factory.Faker('pydict', value_types=['float'], nb_elements=5)