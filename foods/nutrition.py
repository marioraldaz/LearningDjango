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

    