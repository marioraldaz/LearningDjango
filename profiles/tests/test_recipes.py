import pytest
from ..user_recipe import UserRecipe
    
@pytest.mark.django_db
def test_user_recipe_complex(create_user_profile):
    # Create a UserProfile instance for the UserRecipe
    user_profile = create_user_profile

    # Test creating a UserRecipe instance
    user_recipe = UserRecipe.objects.create(
        profile=user_profile,
        title='Test Recipe',
        ingredients='Ingredient 1, Ingredient 2',
        instructions='Step 1: Do something\nStep 2: Do something else'
    )

    # Verify initial attributes
    assert UserRecipe.objects.count() == 1
    assert user_recipe.title == 'Test Recipe'
    assert user_recipe.ingredients == 'Ingredient 1, Ingredient 2'
    assert user_recipe.instructions == 'Step 1: Do something\nStep 2: Do something else'

    # Test str method
    assert str(user_recipe) == 'Test Recipe'

    # Test unique constraint on recipe_id
    with pytest.raises(Exception):
        UserRecipe.objects.create(recipe_id=1, profile=user_profile, title='Duplicate Recipe')

    # Update attributes and verify changes
    user_recipe.title = 'Updated Recipe Title'
    user_recipe.save()
    assert UserRecipe.objects.count() == 1
    assert user_recipe.title == 'Updated Recipe Title'

    # Test relationship with UserProfile
    assert user_recipe.profile == user_profile

    # Clean up after the test
    user_recipe.delete()
