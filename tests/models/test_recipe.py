import pytest
from foods.recipe import Recipe

@pytest.fixture
def recipe_data():
    return {
        "title": "Delicious Recipe",
        "image": "https://example.com/image.jpg",
        "servings": 4,
        "readyInMinutes": 30,
        "instructions": "Cook it well!",
        "spoonacular_id": 12345,
        "sourceName": "Food Blog",
        "sourceUrl": "https://example.com/recipe",
        "healthScore": 8.5,
        "spoonacularScore": 9.2,
        "pricePerServing": 2.5,
        "analyzedInstructions": {"step1": "Do this", "step2": "Then do that"},
        "cheap": True,
        "creditsText": "Credits to the chef",
        "cuisines": ["Italian", "French"],
        "dairyFree": True,
        "diets": ["Vegetarian", "Vegan"],
        "gaps": "No",
        "glutenFree": True,
        "ketogenic": False,
        "lowFodmap": True,
        "occasions": ["Dinner", "Party"],
        "sustainable": True,
        "vegan": True,
        "vegetarian": True,
        "veryHealthy": True,
        "veryPopular": True,
        "whole30": False,
        "weightWatcherSmartPoints": 5,
        "dishTypes": ["Main Dish", "Side Dish"],
        "summary": "This is a delicious recipe.",
        "winePairing": {"pairing1": "Wine A", "pairing2": "Wine B"},
        "nutrition": {
            "nutrients": {"protein": 20, "fat": 10, "carbohydrate": 30}
        }
    }

@pytest.mark.django_db
def test_creation_recipe_without_ingredients(recipe_data):
    # Create a Recipe object with associated Nutrition (without ingredients)
    recipe = Recipe.create_with_nutrition(recipe_data)

    # Validate that the Recipe is created successfully
    assert recipe is not None

    # Validate that the Recipe has the expected attributes
    assert recipe.title == "Delicious Recipe"
    assert recipe.image == "https://example.com/image.jpg"
    assert recipe.servings == 4
    assert recipe.readyInMinutes == 30
    assert recipe.instructions == "Cook it well!"
    assert recipe.spoonacular_id == 12345
    assert recipe.sourceName == "Food Blog"
    assert recipe.sourceUrl == "https://example.com/recipe"
    assert recipe.healthScore == 8.5
    assert recipe.spoonacularScore == 9.2
    assert recipe.pricePerServing == 2.5
    assert recipe.cheap is True
    assert recipe.creditsText == "Credits to the chef"
    assert recipe.cuisines == ["Italian", "French"]
    assert recipe.dairyFree is True
    assert recipe.diets == ["Vegetarian", "Vegan"]
    assert recipe.gaps == "No"
    assert recipe.glutenFree is True
    assert recipe.ketogenic is False
    assert recipe.lowFodmap is True
    assert recipe.occasions == ["Dinner", "Party"]
    assert recipe.sustainable is True
    assert recipe.vegan is True
    assert recipe.vegetarian is True
    assert recipe.veryHealthy is True
    assert recipe.veryPopular is True
    assert recipe.whole30 is False
    assert recipe.weightWatcherSmartPoints == 5
    assert recipe.dishTypes == ["Main Dish", "Side Dish"]
    assert recipe.summary == "This is a delicious recipe."
    assert recipe.winePairing == {"pairing1": "Wine A", "pairing2": "Wine B"}

    # Validate that the Recipe has associated Nutrition
    assert recipe.nutrition is not None
    assert recipe.nutrition.nutrients == {"protein": 20, "fat": 10, "carbohydrate": 30}

    # Validate that the Recipe has no associated ingredients
    assert recipe.ingredients.count() == 0
    
    
@pytest.mark.django_db
@pytest.mark.parametrize("invalid_data, error_field", [
    ({"title": ""}, "title"),  # Empty title
    ({"image": "invalid_url"}, "image"),  # Invalid image URL
    ({"servings": -1}, "servings"),  # Negative servings
    ({"readyInMinutes": -10}, "readyInMinutes"),  # Negative readyInMinutes
    ({"healthScore": "invalid"}, "healthScore"),  # Invalid healthScore (non-float)
    ({"spoonacularScore": "invalid"}, "spoonacularScore"),  # Invalid spoonacularScore (non-float)
    ({"pricePerServing": "invalid"}, "pricePerServing"),  # Invalid pricePerServing (non-float)
    ({"cuisines": "invalid"}, "cuisines"),  # Invalid cuisines (non-list)
    ({"diets": "invalid"}, "diets"),  # Invalid diets (non-list)
    ({"gaps": 123}, "gaps"),  # Invalid gaps (non-string)
    ({"weightWatcherSmartPoints": "invalid"}, "weightWatcherSmartPoints"),  # Invalid weightWatcherSmartPoints (non-int)
    # Add more test cases for other fields
])
def test_recipe_validation_errors(invalid_data, error_field, recipe_factory):
    # Create a recipe using the recipe_factory with the specified invalid_data
    with pytest.raises(Exception):  # Replace Exception with the appropriate error type
        recipe = recipe_factory(**invalid_data)