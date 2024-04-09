

class IngredientView:
    def save_ingredient(self, data):
        # Extract relevant information from the provided JSON data
        ingredient_id = data.get('id')
        name = data.get('name')
        amount = data.get('amount')
        unit = data.get('unit')

        # Save the ingredient to your database or perform other actions
        # Here, we are just returning a dictionary with the saved ingredient information
        saved_ingredient = {
            'ingredient_id': ingredient_id,
            'name': name,
            'amount': amount,
            'unit': unit,
            'message': 'Ingredient saved successfully'
        }

        # Return the saved ingredient information
        return saved_ingredient

    def save_nutrition(self, data):
        # Extract nutrition information from the provided JSON data
        nutrients = data['nutrition']['nutrients']
        properties = data['nutrition']['properties']
        flavonoids = data['nutrition']['flavonoids']
        caloric_breakdown = data['nutrition']['caloricBreakdown']
        weight_per_serving = data['nutrition']['weightPerServing']

        # Save the nutrition information to your database or perform other actions
        # Here, we are just returning a dictionary with the saved nutrition information
        saved_nutrition = {
            'nutrients': nutrients,
            'properties': properties,
            'flavonoids': flavonoids,
            'caloric_breakdown': caloric_breakdown,
            'weight_per_serving': weight_per_serving,
            'message': 'Nutrition information saved successfully'
        }

        # Return the saved nutrition information
        return saved_nutrition

    def post(self, request):
        # Get the JSON data from the request
        data = request.json()

        # Save the ingredient and its associated nutrition information
        saved_ingredient = self.save_ingredient(data)
        saved_nutrition = self.save_nutrition(data)

        # Combine the saved ingredient and nutrition information into a single response
        response_data = {
            'ingredient': saved_ingredient,
            'nutrition': saved_nutrition
        }

        # Return a JSON response with the saved ingredient and nutrition information
        return response_data
    r
    def get_recipe_by_id(self, spoonacular_id):
        # Check if the recipe exists in the database
        if spoonacular_id in self.recipe_database:
            return self.recipe_database[spoonacular_id]
        else:
            return None
