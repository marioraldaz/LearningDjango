from collections import defaultdict
from django.db import models
from django.utils import timezone
from datetime import timedelta
from profiles.user_profile import UserProfile
from django.db import models
class NutritionStatsManager(models.Manager):
    def create_or_update(self, profile):
        obj, created = self.get_or_create(profile=profile)
        return obj
class NutritionStats(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    objects = NutritionStatsManager()

    # Last week nutrient fields
    last_week_calories = models.FloatField(null=True, blank=True)
    last_week_fat = models.FloatField(null=True, blank=True)
    last_week_saturated_fat = models.FloatField(null=True, blank=True)
    last_week_carbohydrates = models.FloatField(null=True, blank=True)
    last_week_sugar = models.FloatField(null=True, blank=True)
    last_week_protein = models.FloatField(null=True, blank=True)
    last_week_cholesterol = models.FloatField(null=True, blank=True)
    last_week_sodium = models.FloatField(null=True, blank=True)
    last_week_fiber = models.FloatField(null=True, blank=True)
    last_week_vitamin_c = models.FloatField(null=True, blank=True)
    last_week_manganese = models.FloatField(null=True, blank=True)
    last_week_folate = models.FloatField(null=True, blank=True)
    last_week_potassium = models.FloatField(null=True, blank=True)
    last_week_magnesium = models.FloatField(null=True, blank=True)
    last_week_vitamin_a = models.FloatField(null=True, blank=True)
    last_week_vitamin_b6 = models.FloatField(null=True, blank=True)
    last_week_vitamin_b12 = models.FloatField(null=True, blank=True)
    last_week_vitamin_d = models.FloatField(null=True, blank=True)
    last_week_calcium = models.FloatField(null=True, blank=True)
    last_week_iron = models.FloatField(null=True, blank=True)
    last_week_zinc = models.FloatField(null=True, blank=True)
    last_week_vitamin_e = models.FloatField(null=True, blank=True)
    last_week_vitamin_k = models.FloatField(null=True, blank=True)
    last_week_omega_3 = models.FloatField(null=True, blank=True)
    last_week_omega_6 = models.FloatField(null=True, blank=True)
    # Add other nutrient fields for last week as needed...

    # Last 30 days nutrient fields
    last_30_days_calories = models.FloatField(null=True, blank=True)
    last_30_days_fat = models.FloatField(null=True, blank=True)
    last_30_days_saturated_fat = models.FloatField(null=True, blank=True)
    last_30_days_carbohydrates = models.FloatField(null=True, blank=True)
    last_30_days_sugar = models.FloatField(null=True, blank=True)
    last_30_days_protein = models.FloatField(null=True, blank=True)
    last_30_days_cholesterol = models.FloatField(null=True, blank=True)
    last_30_days_sodium = models.FloatField(null=True, blank=True)
    last_30_days_fiber = models.FloatField(null=True, blank=True)
    last_30_days_vitamin_c = models.FloatField(null=True, blank=True)
    last_30_days_manganese = models.FloatField(null=True, blank=True)
    last_30_days_folate = models.FloatField(null=True, blank=True)
    last_30_days_potassium = models.FloatField(null=True, blank=True)
    last_30_days_magnesium = models.FloatField(null=True, blank=True)
    last_30_days_vitamin_a = models.FloatField(null=True, blank=True)
    last_30_days_vitamin_b6 = models.FloatField(null=True, blank=True)
    last_30_days_vitamin_b12 = models.FloatField(null=True, blank=True)
    last_30_days_vitamin_d = models.FloatField(null=True, blank=True)
    last_30_days_calcium = models.FloatField(null=True, blank=True)
    last_30_days_iron = models.FloatField(null=True, blank=True)
    last_30_days_zinc = models.FloatField(null=True, blank=True)
    last_30_days_vitamin_e = models.FloatField(null=True, blank=True)
    last_30_days_vitamin_k = models.FloatField(null=True, blank=True)
    last_30_days_omega_3 = models.FloatField(null=True, blank=True)
    last_30_days_omega_6 = models.FloatField(null=True, blank=True)
    
    @classmethod
    def create_or_update(cls, profile):
        obj, created = cls.objects.update_or_create(profile=profile)
        return obj


    def compute_last_week_nutrients(self):
        end_date = timezone.now().date()
        start_date = end_date - timedelta(days=7)
        user_dailies = self.profile.userdaily_set.filter(date__range=[start_date, end_date])

        self.compute_total_nutrients(user_dailies, 'last_week')

    def compute_last_30_days_nutrients(self):
        end_date = timezone.now().date()
        start_date = end_date - timedelta(days=30)
        user_dailies = self.profile.userdaily_set.filter(date__range=[start_date, end_date])

        self.compute_total_nutrients(user_dailies, 'last_30_days')
    def compute_nutrients(self, days, time_period):
        end_date = timezone.now().date()
        start_date = end_date - timedelta(days=days)
        user_dailies = self.profile.userdaily_set.filter(date__range=[start_date, end_date])

        total_nutrients = defaultdict(float)

        for user_daily in user_dailies:
            if user_daily.total_nutrients:
                for nutrient, amount in user_daily.total_nutrients.items():
                    total_nutrients[nutrient] += amount

        nutrient_fields = {
            'calories': f'{time_period}_calories',
            'fat': f'{time_period}_fat',
            'saturated_fat': f'{time_period}_saturated_fat',
            'carbohydrates': f'{time_period}_carbohydrates',
            'sugar': f'{time_period}_sugar',
            'protein': f'{time_period}_protein',
            'cholesterol': f'{time_period}_cholesterol',
            'sodium': f'{time_period}_sodium',
            'fiber': f'{time_period}_fiber',
            'vitamin_c': f'{time_period}_vitamin_c',
            'manganese': f'{time_period}_manganese',
            'folate': f'{time_period}_folate',
            'potassium': f'{time_period}_potassium',
            'magnesium': f'{time_period}_magnesium',
            'vitamin_a': f'{time_period}_vitamin_a',
            'vitamin_b6': f'{time_period}_vitamin_b6',
            'vitamin_b12': f'{time_period}_vitamin_b12',
            'vitamin_d': f'{time_period}_vitamin_d',
            'calcium': f'{time_period}_calcium',
            'iron': f'{time_period}_iron',
            'zinc': f'{time_period}_zinc',
            'vitamin_e': f'{time_period}_vitamin_e',
            'vitamin_k': f'{time_period}_vitamin_k',
            'omega_3': f'{time_period}_omega_3',
            'omega_6': f'{time_period}_omega_6',
            # Add other nutrient fields mapping as needed...
        }

        for nutrient, model_field in nutrient_fields.items():
            setattr(self, model_field, total_nutrients.get(nutrient.replace('_', ' ').title(), 0))

        self.save()

    def compute_last_week_nutrients(self):
        self.compute_nutrients(7, 'last_week')

    def compute_last_30_days_nutrients(self):
        self.compute_nutrients(30, 'last_30_days')

        self.save()
        
    def compute_stats(self):
        self.compute_last_week_nutrients()
        self.compute_last_30_days_nutrients()
