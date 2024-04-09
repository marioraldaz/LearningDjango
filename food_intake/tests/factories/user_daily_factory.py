import factory
from django.utils import timezone
from faker import Faker  # Import Faker
from food_intake.user_daily import UserDaily
from profiles.user_profile import UserProfile
from profiles.factories.profile_factory import ProfileFactory
fake = Faker()  # Initialize Faker
    
class UserDailyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserDaily

    profile = factory.SubFactory(ProfileFactory)  
    date = factory.LazyFunction(timezone.now().date)
    total_calories_consumed = fake.random_int(min=1000, max=5000)  # Random integer between 1000 and 5000
    total_protein_consumed = fake.random_int(min=50, max=200)  # Random integer between 50 and 200
    total_fat_consumed = fake.random_int(min=20, max=100)  # Random integer between 20 and 100
    total_carbohydrates_consumed = fake.random_int(min=100, max=300)  # Random integer between 100 and 300
    

class UserDailyNegativeValuesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserDaily

    profile = factory.SubFactory(ProfileFactory)
    date = fake.date_this_year()
    total_calories_consumed = fake.random_int(min=-1000, max=-1)  # Negative value
    total_protein_consumed = fake.random_int(min=-1000, max=-1)  # Negative value
    total_fat_consumed = fake.random_int(min=-1000, max=-1)  # Negative value
    total_carbohydrates_consumed = fake.random_int(min=-1000, max=-1)  # Negative value