class RecipeView:
    def save_recipe(self, data):
        # Extract relevant information from the provided JSON data
        recipe_id = data.get('id')
        title = data.get('title')
        servings = data.get('servings')
        ready_in_minutes = data.get('readyInMinutes')
        source_name = data.get('sourceName')
        source_url = data.get('sourceUrl')

        # Save the recipe to your database or perform other actions
        # Here, we are just returning a dictionary with the saved recipe information
        saved_recipe = {
            'recipe_id': recipe_id,
            'title': title,
            'servings': servings,
            'ready_in_minutes': ready_in_minutes,
            'source_name': source_name,
            'source_url': source_url,
            'message': 'Recipe saved successfully'
        }

        # Return the saved recipe information
        return saved_recipe

    def save_extended_ingredients(self, data):
        # Extract extended ingredients information from the provided JSON data
        extended_ingredients = data.get('extendedIngredients')

        # Save the extended ingredients to your database or perform other actions
        # Here, we are just returning a dictionary with the saved extended ingredients information
        saved_extended_ingredients = {
            'extended_ingredients': extended_ingredients,
            'message': 'Extended ingredients saved successfully'
        }

        # Return the saved extended ingredients information
        return saved_extended_ingredients

    def save_nutrition(self, data):
        # Extract nutrition information from the provided JSON data
        nutrition = data.get('nutrition')

        # Save the nutrition information to your database or perform other actions
        # Here, we are just returning a dictionary with the saved nutrition information
        saved_nutrition = {
            'nutrition': nutrition,
            'message': 'Nutrition information saved successfully'
        }

        # Return the saved nutrition information
        return saved_nutrition

    def post(self, request):
        # Get the JSON data from the request
        data = request.json()

        # Save the recipe, extended ingredients, and nutrition information
        saved_recipe = self.save_recipe(data)
        saved_extended_ingredients = self.save_extended_ingredients(data)
        saved_nutrition = self.save_nutrition(data)

        # Combine the saved recipe, extended ingredients, and nutrition information into a single response
        response_data = {
            'recipe': saved_recipe,
            'extended_ingredients': saved_extended_ingredients,
            'nutrition': saved_nutrition
        }

        # Return a JSON response with the saved recipe, extended ingredients, and nutrition information
        return response_data