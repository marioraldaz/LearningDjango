
from django.db import models

class UserDaily(models.Model):
    date = models.DateField()
    total_nutrients = models.JSONField(null=True, blank=True)
    total_properties = models.JSONField(null=True, blank=True)
    total_flavonoids = models.JSONField(null=True, blank=True)
    total_caloric_breakdown = models.JSONField(null=True, blank=True)
    total_weight_per_serving = models.JSONField(null=True, blank=True)

    def calculate_and_save_nutrition(self):
        total_nutrients = {}
        total_properties = {}
        total_flavonoids = {}
        total_caloric_breakdown = {}
        total_weight_per_serving = {}

        # Iterate over all FoodIntake instances associated with this UserDaily
        for food_intake in self.foodintake_set.all():
            for food_intake_detail in food_intake.foodintakedetail_set.all():
                if food_intake_detail.ingredient:
                    ingredient_nutrition = food_intake_detail.ingredient.nutrition
                    # Add ingredient nutrition to total nutrition
                    for key, value in ingredient_nutrition.items():
                        total_nutrients[key] = total_nutrients.get(key, 0) + value.get('nutrients', 0)
                        total_properties[key] = total_properties.get(key, 0) + value.get('properties', 0)
                        total_flavonoids[key] = total_flavonoids.get(key, 0) + value.get('flavonoids', 0)
                        total_caloric_breakdown[key] = total_caloric_breakdown.get(key, 0) + value.get('caloricBreakdown', 0)
                        total_weight_per_serving[key] = total_weight_per_serving.get(key, 0) + value.get('weightPerServing', 0)
                elif food_intake_detail.recipe:
                    recipe_nutrition = food_intake_detail.recipe.nutrition
                    # Add recipe nutrition to total nutrition
                    for key, value in recipe_nutrition.items():
                        total_nutrients[key] = total_nutrients.get(key, 0) + value.get('nutrients', 0)
                        total_properties[key] = total_properties.get(key, 0) + value.get('properties', 0)
                        total_flavonoids[key] = total_flavonoids.get(key, 0) + value.get('flavonoids', 0)
                        total_caloric_breakdown[key] = total_caloric_breakdown.get(key, 0) + value.get('caloricBreakdown', 0)
                        total_weight_per_serving[key] = total_weight_per_serving.get(key, 0) + value.get('weightPerServing', 0)

        # Save the total nutrition to the UserDaily instance
        self.total_nutrients = total_nutrients
        self.total_properties = total_properties
        self.total_flavonoids = total_flavonoids
        self.total_caloric_breakdown = total_caloric_breakdown
        self.total_weight_per_serving = total_weight_per_serving
        self.save()