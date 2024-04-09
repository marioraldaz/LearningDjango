from django.db import models

class Nutrition(models.Model):
    nutrients = models.JSONField()
    properties = models.JSONField()
    flavonoids = models.JSONField()
    caloricBreakdown = models.JSONField()
    weightPerServing = models.JSONField()


    