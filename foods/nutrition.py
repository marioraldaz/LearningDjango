from django.db import models

class Nutrition(models.Model):
      # Fields for nutrients
    nutrients = models.JSONField()
    
    # Fields for properties
    properties = models.JSONField()
    
    # Fields for flavonoids
    flavonoids = models.JSONField()
    
    # Field for caloric breakdown
    percent_protein = models.FloatField()
    percent_fat = models.FloatField()
    percent_carbs = models.FloatField()
    
    # Field for weight per serving
    weight_per_serving = models.JSONField()

    @classmethod
    def create_from_json(cls, nutrition_data):
        # Extract necessary data from nutrition_data JSON
        nutrients = nutrition_data.get('nutrients')
        properties = nutrition_data.get('properties')
        flavonoids = nutrition_data.get('flavonoids')
        percent_protein = nutrition_data.get('caloricBreakdown', {}).get('percentProtein')
        percent_fat = nutrition_data.get('caloricBreakdown', {}).get('percentFat')
        percent_carbs = nutrition_data.get('caloricBreakdown', {}).get('percentCarbs')
        weight_per_serving = nutrition_data.get('weightPerServing')

        # Create and return a new Nutrition object
        return cls.objects.create(
            nutrients=nutrients,
            properties=properties,
            flavonoids=flavonoids,
            percent_protein=percent_protein,
            percent_fat=percent_fat,
            percent_carbs=percent_carbs,
            weight_per_serving=weight_per_serving
        )