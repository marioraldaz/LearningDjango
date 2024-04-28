from django.db import models
from django.core.exceptions import ValidationError
from profiles.user_profile import UserProfile
from datetime import timedelta

class UserDaily(models.Model):
    date = models.DateField()
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True) 
    total_nutrients = models.JSONField(null=True, blank=True)
    total_properties = models.JSONField(null=True, blank=True)
    total_flavonoids = models.JSONField(null=True, blank=True)
    total_caloric_breakdown = models.JSONField(null=True, blank=True)
    total_weight_per_serving = models.JSONField(null=True, blank=True)


    def sum_nutrition_data(self):
        total_nutrients = {}
        total_properties = {}
        total_flavonoids = {}
        total_caloric_breakdown = {
            'percentProtein': 0,
            'percentFat': 0,
            'percentCarbs': 0
        }
        total_weight_per_serving = {
            'amount': 0,
            'unit': 'g'
        }

        food_intakes = self.foodintake_set.all()

        for food_intake in food_intakes:
            for food_intake_detail in food_intake.details.all():
                nutrients_data = food_intake_detail.get_nutrients_data()
                properties_data = food_intake_detail.get_properties_data()
                flavonoids_data = food_intake_detail.get_flavonoids_data()
                caloric_breakdown_data = food_intake_detail.get_caloric_breakdown_data()
                weight_per_serving_data = food_intake_detail.get_weight_per_serving_data()

                # Sum nutrients data
                for nutrient, amount in nutrients_data.items():
                    total_nutrients[nutrient] = total_nutrients.get(nutrient, 0) + amount

                # Sum properties data
                for prop, amount in properties_data.items():
                    total_properties[prop] = total_properties.get(prop, 0) + amount

                # Sum flavonoids data
                for flavonoid, amount in flavonoids_data.items():
                    total_flavonoids[flavonoid] = total_flavonoids.get(flavonoid, 0) + amount

                # Sum caloric breakdown data
                total_caloric_breakdown['percentProtein'] += caloric_breakdown_data.get('percentProtein', 0)
                total_caloric_breakdown['percentFat'] += caloric_breakdown_data.get('percentFat', 0)
                total_caloric_breakdown['percentCarbs'] += caloric_breakdown_data.get('percentCarbs', 0)

                # Sum weight per serving data
                total_weight_per_serving['amount'] += weight_per_serving_data.get('amount', 0)

        # Normalize caloric breakdown data
        total_caloric_breakdown = {key: value / len(food_intakes) for key, value in total_caloric_breakdown.items()}


        # Check for negative values
        for value in total_nutrients.values():
            if value < 0:
                raise ValidationError("Negative value found in total nutrients.")

        for value in total_properties.values():
            if value < 0:
                raise ValidationError("Negative value found in total properties.")

        for value in total_flavonoids.values():
            if value < 0:
                raise ValidationError("Negative value found in total flavonoids.")

        for value in total_caloric_breakdown.values():
            if value < 0:
                raise ValidationError("Negative value found in total caloric breakdown.")

        if total_weight_per_serving['amount'] < 0:
            raise ValidationError("Negative value found in total weight per serving.")

        return {
            'total_nutrients': total_nutrients,
            'total_properties': total_properties,
            'total_flavonoids': total_flavonoids,
            'total_caloric_breakdown': total_caloric_breakdown,
            'total_weight_per_serving': total_weight_per_serving
        }
        
    @classmethod
    def get_last_days(cls, profile_id, num_days):
        """Return UserDaily objects for the last 'num_days' days for a given UserProfile ID."""
        from_date = models.DateField.auto_now() - timedelta(days=num_days)
        user_dailies = cls.objects.filter(profile_id=profile_id, date__gte=from_date)
        return user_dailies