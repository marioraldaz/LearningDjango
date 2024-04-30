import factory
from django.contrib.contenttypes.models import ContentType
from food_intake.food_intake_detail import FoodIntakeDetail
from .food_intake_factory import FoodIntakeFactory
from .ingredient_factory import IngredientFactory
from .recipe_factory import RecipeFactory

class FoodIntakeDetailFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = FoodIntakeDetail

    food_intake = factory.SubFactory(FoodIntakeFactory) 
    content_type = factory.Iterator(ContentType.objects.filter(app_label='food_intake', model__in=['ingredient', 'recipe']))
    ingredient = factory.SubFactory(IngredientFactory)
    recipe = factory.SubFactory(RecipeFactory)
    amount = factory.Faker('random_int', min=0, max=100)
    