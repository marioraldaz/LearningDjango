from django.db import models

class Nutrition(models.Model):
      # Fields for nutrients
    nutrients =  models.JSONField(null=True, blank=True)
    
    # Fields for properties
    properties = models.JSONField(null=True, blank=True)
    
    # Fields for flavonoids
    flavonoids = models.JSONField(null=True, blank=True)
    
    # Field for caloric breakdown
    percent_protein = models.FloatField(null=True, blank=True)
    percent_fat = models.FloatField(null=True, blank=True)
    percent_carbs = models.FloatField(null=True, blank=True)
    
    # Field for weight per serving
    weight_per_serving =  models.JSONField(null=True, blank=True)

    @classmethod
    def create_from_json(cls, nutrition_data):
        # Extract necessary data from nutrition_data JSON
        nutrients = nutrition_data.get('nutrients', {})
        properties = nutrition_data.get('properties', {})
        flavonoids = nutrition_data.get('flavonoids', {})
        
        # Get caloric breakdown data
        caloric_breakdown = nutrition_data.get('caloricBreakdown', {})
        percent_protein = caloric_breakdown.get('percentProtein',0.0)
        percent_fat = caloric_breakdown.get('percentFat',0.0)
        percent_carbs = caloric_breakdown.get('percentCarbs', 0.0)  # Default to 0.0 if not provided
        weight_per_serving = nutrition_data.get('weightPerServing', {})

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