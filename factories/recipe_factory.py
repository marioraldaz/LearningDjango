import factory
from foods.recipe import Recipe
from factories.nutrition_factory import NutritionFactory


class RecipeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Recipe

    nutrition = factory.SubFactory(NutritionFactory)
    title = factory.Faker('sentence', nb_words=4, variable_nb_words=True)
    image = factory.Faker('image_url')
    servings = factory.Faker('random_digit_not_null')
    readyInMinutes = factory.Faker('random_int', min=0, max=300)
    instructions = factory.Faker('text')
    spoonacular_id = factory.Sequence(lambda n: n)
    sourceName = factory.Faker('company')
    sourceUrl = factory.Faker('url')
    healthScore = factory.Faker('pyfloat', left_digits=2, right_digits=2, positive=True)
    spoonacularScore = factory.Faker('pyfloat', left_digits=2, right_digits=2, positive=True)
    pricePerServing = factory.Faker('pyfloat', left_digits=2, right_digits=2, positive=True)
    analyzedInstructions = factory.Faker('pydict', value_types=['str'], nb_elements=5)
    cheap = factory.Faker('boolean')
    creditsText = factory.Faker('text', max_nb_chars=200)
    cuisines = fact
