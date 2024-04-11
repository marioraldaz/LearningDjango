import factory
from faker import Faker
from profiles.user_profile import UserProfile

fake = Faker()

class UserProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserProfile

    username = factory.Sequence(lambda n: f'user{n}')  # Generate unique usernames like 'user1', 'user2', etc.
    password = factory.Faker('password', length=12)  # Generate random passwords
    gender = factory.Faker('random_element', elements=['Male', 'Female'])  # Random gender
    email = factory.LazyAttribute(lambda obj: f'{obj.username}@example.com')  # Email based on username
    weight = factory.Faker('random_int', min=50, max=150)  # Random weight between 50 and 150
    height = factory.Faker('random_int', min=150, max=200)  # Random height between 150 and 200
    date_of_birth = factory.Faker('date_of_birth')  # Random date of birth
    activityLevel = factory.Faker('random_int', min=1, max=5)  # Random activity level between 1 and 5
    
