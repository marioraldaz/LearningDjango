import factory
from faker import Faker
from factories.user_profile_factory import UserProfileFactory
from profiles.profile_fitness import UserFitnessProfile

faker = Faker()

class UserFitnessProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserFitnessProfile

    user_profile = factory.SubFactory(UserProfileFactory)  # Assuming UserProfileFactory is defined
    goal = factory.Iterator([choice[0] for choice in UserFitnessProfile.GOAL_CHOICES])
    daily_calorie_intake_goal = factory.LazyFunction(lambda: faker.random_int(min=1500, max=3000))
    daily_protein_goal = factory.LazyFunction(lambda: faker.pyfloat(left_digits=2, right_digits=1, positive=True))
    daily_fat_goal = factory.LazyFunction(lambda: faker.pyfloat(left_digits=2, right_digits=1, positive=True))
    daily_carbohydrate_goal = factory.LazyFunction(lambda: faker.pyfloat(left_digits=2, right_digits=1, positive=True))
    activity_level = factory.Iterator([1, 2, 3, 4, 5])

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        """
        Override default _create method to handle related fields
        """
        user_profile = kwargs.pop('user_profile', None)
        if user_profile is None:
            user_profile = UserProfileFactory()  # Create a new UserProfile if not provided

        return model_class.objects.create(user_profile=user_profile, *args, **kwargs)
