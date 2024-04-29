import pytest
from foods.recipe import Recipe

# Define test data for Recipe creation
test_data = [
    {
        "title": "Pasta Carbonara",
        "image": "https://example.com/pasta.jpg",
        "servings": 4,
        "readyInMinutes": 30,
        "instructions": "Cook pasta. Fry bacon. Mix eggs and cheese. Combine all ingredients.",
        "spoonacular_id": 12345,
        "sourceName": "Italian Recipes",
        "sourceUrl": "https://example.com/pasta-recipes",
        "healthScore": 80.5,
        "spoonacularScore": 90.0,
        "pricePerServing": 2.5,
        "cheap": False,
        "dairyFree": False,
        "diets": ["balanced", "high-protein"],
        "vegetarian": False,
        "extendedIngredients": [{"name": "Pasta", "amount": 200, "unit": "g"}, {"name": "Bacon", "amount": 100, "unit": "g"}]
    },
    # Add more test data as needed
]

# Parametrize the test with the recipe_data
@pytest.mark.django_db
@pytest.mark.parametrize("recipe_data", test_data)
def test_recipe_creation(recipe_data):
    # Create a Recipe instance using the provided recipe_data
    recipe = Recipe.objects.create(
        title=recipe_data["title"],
        image=recipe_data["image"],
        servings=recipe_data["servings"],
        readyInMinutes=recipe_data["readyInMinutes"],
        instructions=recipe_data["instructions"],
        spoonacular_id=recipe_data["spoonacular_id"],
        sourceName=recipe_data["sourceName"],
        sourceUrl=recipe_data["sourceUrl"],
        healthScore=recipe_data["healthScore"],
        spoonacularScore=recipe_data["spoonacularScore"],
        pricePerServing=recipe_data["pricePerServing"],
        cheap=recipe_data["cheap"],
        dairyFree=recipe_data["dairyFree"],
        vegetarian=recipe_data["vegetarian"]
        # Add other fields as necessary
    )

    # Validate the Recipe instance properties
    assert recipe is not None
    assert recipe.title == recipe_data["title"]
    assert recipe.image == recipe_data["image"]
    assert recipe.servings == recipe_data["servings"]
    assert recipe.readyInMinutes == recipe_data["readyInMinutes"]
    assert recipe.instructions == recipe_data["instructions"]
    assert recipe.spoonacular_id == recipe_data["spoonacular_id"]
    assert recipe.sourceName == recipe_data["sourceName"]
    assert recipe.sourceUrl == recipe_data["sourceUrl"]
    assert recipe.healthScore == pytest.approx(recipe_data["healthScore"], abs=0.01)
    assert recipe.spoonacularScore == pytest.approx(recipe_data["spoonacularScore"], abs=0.01)
    assert recipe.pricePerServing == pytest.approx(recipe_data["pricePerServing"], abs=0.01)
    assert recipe.cheap == recipe_data["cheap"]
    assert recipe.dairyFree == recipe_data["dairyFree"]
    assert recipe.vegetarian == recipe_data["vegetarian"]

    # Validate extendedIngredients association
    assert recipe.ingredients.count() == len(recipe_data["extendedIngredients"])
    for ingredient_data in recipe_data["extendedIngredients"]:
        ingredient_name = ingredient_data["name"]
        ingredient = recipe.ingredients.filter(name=ingredient_name).first()
        assert ingredient is not None
        assert ingredient.amount == pytest.approx(ingredient_data["amount"], abs=0.01)
        assert ingredient.unit == ingredient_data["unit"]