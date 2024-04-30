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
    cuisines = factory.Faker('pylist', nb_elements=3, variable_nb_elements=True, value_types=['str'])
    dairyFree = factory.Faker('boolean')
    diets = factory.Faker('pylist', nb_elements=3, variable_nb_elements=True, value_types=['str'])
    gaps = factory.Faker('random_element', elements=['Yes', 'No'])
    glutenFree = factory.Faker('boolean')
    ketogenic = factory.Faker('boolean')
    lowFodmap = factory.Faker('boolean')
    occasions = factory.Faker('pylist', nb_elements=3, variable_nb_elements=True, value_types=['str'])
    sustainable = factory.Faker('boolean')
    vegan = factory.Faker('boolean')
    vegetarian = factory.Faker('boolean')
    veryHealthy = factory.Faker('boolean')
    veryPopular = factory.Faker('boolean')
    whole30 = factory.Faker('boolean')
    weightWatcherSmartPoints = factory.Faker('random_int', min=0, max=20)
    dishTypes = factory.Faker('pylist', nb_elements=3, variable_nb_elements=True, value_types=['str'])
    extendedIngredients = factory.Faker('pylist', nb_elements=5, variable_nb_elements=True, value_types=['str'])
    summary = factory.Faker('text')
    winePairing = factory.Faker('pydict', value_types=['str'], nb_elements=5)

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        from decimal import Decimal
        from datetime import datetime
        # Custom JSON encoder for Decimal and datetime objects
        def json_encode(obj):
            if isinstance(obj, Decimal):
                return float(obj)
            elif isinstance(obj, datetime):
                return obj.isoformat()
            else:
                return None

        # Use the custom encoder to serialize kwargs
        serialized_kwargs = {k: json_encode(v) for k, v in kwargs.items()}

        # Create the model instance with serialized kwargs
        return model_class.objects.create(**serialized_kwargs)