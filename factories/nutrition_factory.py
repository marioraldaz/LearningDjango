import json
import factory
from faker import Faker
from foods.nutrition import Nutrition
fake = Faker()

class NutritionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Nutrition

    # Generate a dictionary of nutrients with random names and values
    nutrients = fake.pydict(value_types=[("float", {"min_value": 0, "max_value": 100}), "str"], nb_elements=5)

    # Generate a dictionary of properties with random names and values
    properties = fake.pydict(value_types=[("float", {"min_value": 0, "max_value": 100}), "str"], nb_elements=2)

    # Generate a dictionary of flavonoids with random names and values
    flavonoids = fake.pydict(value_types=[("float", {"min_value": 0, "max_value": 100}), "str"], nb_elements=1)

    # Generate a random floating-point number between 0 and 100 for percent_protein, percent_fat, and percent_carbs
    percent_protein = fake.pyfloat(left_digits=2, right_digits=2, min_value=0, max_value=100)
    percent_fat = fake.pyfloat(left_digits=2, right_digits=2, min_value=0, max_value=100)
    percent_carbs = fake.pyfloat(left_digits=2, right_digits=2, min_value=0, max_value=100)

    # Generate a dictionary with a random floating-point number for the amount and a string for the unit
    weight_per_serving = fake.pydict(value_types=[("float", {"min_value": 0, "max_value": 1000}), "str"])

    @classmethod
    def create(cls, **kwargs):
        # Generate an instance of NutritionFactory
        obj = super().create(**kwargs)
        # Convert nutrients, properties, flavonoids to JSON
        obj.nutrients = json.dumps(obj.nutrients)
        obj.properties = json.dumps(obj.properties)
        obj.flavonoids = json.dumps(obj.flavonoids)
        obj.save()
        return obj
