import factory
from foods.ingredient import Ingredient
from .nutrition_factory import NutritionFactory

class IngredientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ingredient

    nutrition = factory.SubFactory(NutritionFactory)
    name = factory.Faker('word')
    spoonacular_id = factory.Sequence(lambda n: n)
    original = factory.Faker('sentence', nb_words=6, variable_nb_words=True)
    originalName = factory.Faker('sentence', nb_words=6, variable_nb_words=True)
    amount = factory.Faker('pyfloat', left_digits=2, right_digits=2, positive=True)
    unit = factory.Faker('word')
    unitShort = factory.Faker('word')
    unitLong = factory.Faker('word')
    possibleUnits = factory.Faker('pydict', value_types=['str'], nb_elements=5)
    estimatedCost_value = factory.Faker('pyfloat', left_digits=2, right_digits=2, positive=True)
    estimatedCost_unit = factory.Faker('word')
    consistency = factory.Faker('word')
    shoppingListUnits = factory.Faker('pydict', value_types=['str'], nb_elements=5)
    aisle = factory.Faker('word')
    image = factory.Faker('url')
    meta = factory.Faker('pydict', value_types=['str'], nb_elements=5)
    categoryPath = factory.Faker('pydict', value_types=['str'], nb_elements=5)
