from collections import defaultdict
import json
from django.db import models
from django.core.exceptions import ValidationError
from food_intake.food_intake import FoodIntake
from foods.nutrition import Nutrition
from foods.recipe import Recipe
from profiles.user_profile import UserProfile
from datetime import timedelta
from utils.validators import  validate_is_date_before_today
from django.core.serializers import serialize
from django.db import models

class UserDailyManager(models.Manager):
    def update_or_create(self, defaults=None, **kwargs):
        instance, created = super().update_or_create(defaults=defaults, **kwargs)
        instance.sum_nutrition_data()
        instance.save()
        return instance, created
    
class UserDaily(models.Model):
    date = models.DateField(validators=[validate_is_date_before_today], primary_key=True)
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True) 
    total_nutrients = models.JSONField(null=True, blank=True)
    total_properties = models.JSONField(null=True, blank=True)
    total_flavonoids = models.JSONField(null=True, blank=True)
    total_caloric_breakdown = models.JSONField(null=True, blank=True)
    total_weight_per_serving = models.JSONField(null=True, blank=True)
    objects = UserDailyManager()  # Use the custom manager



    def sum_nutrition_data(self):
        total_nutrients = defaultdict(float)
        total_properties = defaultdict(float)
        total_flavonoids = defaultdict(float)
        total_caloric_breakdown = {
            'percent_proteins': 0.0,
            'percent_fat': 0.0,
            'percent_carbs': 0.0
        }
        total_weight_per_serving = {
            'amount': 0.0,
            'unit': 'g'
        }

        food_intakes = FoodIntake.get_food_intakes_for_user_and_date(self.profile, self.date)

        for food_intake in food_intakes:
            for food_intake_detail in food_intake.foodintakedetail_set.all():
            
                nutrients_data = food_intake_detail.get_nutrients_data()
                properties_data = food_intake_detail.get_properties_data()
                flavonoids_data = food_intake_detail.get_flavonoids_data()
                caloric_breakdown_data = food_intake_detail.get_caloric_breakdown_data()
                weight_per_serving_data = food_intake_detail.get_weight_per_serving_data()

                # Sum nutrients data
                for nutrient in nutrients_data:
                    name = nutrient['name']
                    amount = nutrient['amount']
                    total_nutrients[name] += amount

                # Sum properties data
                for prop in properties_data:
                    name = prop['name']
                    amount = prop['amount']
                    total_properties[name] += amount

                # Sum flavonoids data
                for flavonoid in flavonoids_data:
                    name = flavonoid['name']
                    amount = flavonoid['amount']
                    total_flavonoids[name] += amount
                # Sum caloric breakdown data
                total_caloric_breakdown['percent_proteins'] += caloric_breakdown_data['percent_proteins']
                total_caloric_breakdown['percent_fat'] += caloric_breakdown_data['percent_fat']
                total_caloric_breakdown['percent_carbs'] += caloric_breakdown_data['percent_carbs']

                # Sum weight per serving data
                
                if 'amount' in weight_per_serving_data:
                    total_weight_per_serving['amount'] += weight_per_serving_data['amount']
                else:
                    total_weight_per_serving['amount'] += weight_per_serving_data[0]['amount']

        # Normalize caloric breakdown data
        if food_intakes:
            num_food_intakes = len(food_intakes)
            total_caloric_breakdown = {key: value / num_food_intakes for key, value in total_caloric_breakdown.items()}    

        self.total_nutrients = dict(total_nutrients)
        self.total_properties = dict(total_properties)
        self.total_flavonoids = dict(total_flavonoids)
        self.total_caloric_breakdown = total_caloric_breakdown
        self.total_weight_per_serving = total_weight_per_serving

        return {
            'total_nutrients': self.total_nutrients,
            'total_properties': self.total_properties,
            'total_flavonoids': self.total_flavonoids,
            'total_caloric_breakdown': self.total_caloric_breakdown,
            'total_weight_per_serving': self.total_weight_per_serving
        }

        
    @classmethod
    def get_last_days(cls, profile_id, num_days):
        """Return UserDaily objects for the last 'num_days' days for a given UserProfile ID."""
        from_date = models.DateField.auto_now() - timedelta(days=num_days)
        user_dailies = cls.objects.filter(profile_id=profile_id, date__gte=from_date)
        return user_dailies
