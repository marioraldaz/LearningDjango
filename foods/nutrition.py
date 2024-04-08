from django.db import models
from .recipe import recipe

class Nutrition(models.Model):
    nutrients = models.JSONField()
    properties = models.JSONField()
    flavonoids = models.JSONField()
    caloricBreakdown = models.JSONField()
    weightPerServing = models.JSONField()

    def process_nutrition_data(nutrition_data):
        processed_data = {}

        # Process nutrients
        nutrients = {}
        for nutrient in nutrition_data.get('nutrients', []):
            name = nutrient['name']
            nutrients[name] = {
                'amount': nutrient['amount'],
                'unit': nutrient['unit'],
                'percentOfDailyNeeds': nutrient['percentOfDailyNeeds']
            }
        processed_data['nutrients'] = nutrients

        # Process properties
        properties = {}
        for prop in nutrition_data.get('properties', []):
            properties[prop['name']] = {
                'amount': prop['amount'],
                'unit': prop['unit']
            }
        processed_data['properties'] = properties

        # Process flavonoids
        flavonoids = {}
        for flavonoid in nutrition_data.get('flavonoids', []):
            flavonoids[flavonoid['name']] = {
                'amount': flavonoid['amount'],
                'unit': flavonoid['unit']
            }
        processed_data['flavonoids'] = flavonoids

        # Process ingredients
        ingredients = {}
        for ingredient in nutrition_data.get('ingredients', []):
            ingredient_id = ingredient['id']
            ingredients[ingredient_id] = {
                'name': ingredient['name'],
                'amount': ingredient['amount'],
                'unit': ingredient['unit']
            }
            ingredient_nutrients = {}
            for nutrient in ingredient.get('nutrients', []):
                nutrient_name = nutrient['name']
                ingredient_nutrients[nutrient_name] = {
                    'amount': nutrient['amount'],
                    'unit': nutrient['unit'],
                    'percentOfDailyNeeds': nutrient['percentOfDailyNeeds']
                }
            ingredients[ingredient_id]['nutrients'] = ingredient_nutrients
        processed_data['ingredients'] = ingredients

        # Process caloric breakdown
        caloric_breakdown = nutrition_data.get('caloricBreakdown', {})
        processed_data['caloricBreakdown'] = {
            'percentProtein': caloric_breakdown.get('percentProtein', 0),
            'percentFat': caloric_breakdown.get('percentFat', 0),
            'percentCarbs': caloric_breakdown.get('percentCarbs', 0)
        }

        # Process weight per serving
        weight_per_serving = nutrition_data.get('weightPerServing', {})
        processed_data['weightPerServing'] = {
            'amount': weight_per_serving.get('amount', 0),
            'unit': weight_per_serving.get('unit', '')
        }

        return processed_data
