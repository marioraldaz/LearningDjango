from django.db import models
from django.utils import timezone
from datetime import timedelta
from profiles.user_profile import UserProfile

class NutritionStats(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    
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
    # Add other nutrient fields for last 30 days as needed...

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

    def compute_total_nutrients(self, user_dailies, time_period):
        total_calories = 0
        total_fat = 0
        total_saturated_fat = 0
        total_carbohydrates = 0
        total_sugar = 0
        total_protein = 0
        total_cholesterol = 0
        total_sodium = 0
        total_fiber = 0
        total_vitamin_c = 0
        total_manganese = 0
        total_folate = 0
        total_potassium = 0
        total_magnesium = 0
        total_vitamin_a = 0
        total_vitamin_b6 = 0
        total_vitamin_b12 = 0
        total_vitamin_d = 0
        total_calcium = 0
        total_iron = 0
        total_zinc = 0
        total_vitamin_e = 0
        total_vitamin_k = 0
        total_omega_3 = 0
        total_omega_6 = 0
        # Add other nutrient total variables as needed...

        for user_daily in user_dailies:
            if user_daily.total_nutrients:
                total_calories += user_daily.total_nutrients.get('Calories', 0)
                total_fat += user_daily.total_nutrients.get('Fat', 0)
                total_saturated_fat += user_daily.total_nutrients.get('Saturated Fat', 0)
                total_carbohydrates += user_daily.total_nutrients.get('Carbohydrates', 0)
                total_sugar += user_daily.total_nutrients.get('Sugar', 0)
                total_protein += user_daily.total_nutrients.get('Protein', 0)
                total_cholesterol += user_daily.total_nutrients.get('Cholesterol', 0)
                total_sodium += user_daily.total_nutrients.get('Sodium', 0)
                total_fiber += user_daily.total_nutrients.get('Fiber', 0)
                total_vitamin_c += user_daily.total_nutrients.get('Vitamin C', 0)
                total_manganese += user_daily.total_nutrients.get('Manganese', 0)
                total_folate += user_daily.total_nutrients.get('Folate', 0)
                total_potassium += user_daily.total_nutrients.get('Potassium', 0)
                total_magnesium += user_daily.total_nutrients.get('Magnesium', 0)
                total_vitamin_a += user_daily.total_nutrients.get('Vitamin A', 0)
                total_vitamin_b6 += user_daily.total_nutrients.get('Vitamin B6', 0)
                total_vitamin_b12 += user_daily.total_nutrients.get('Vitamin B12', 0)
                total_vitamin_d += user_daily.total_nutrients.get('Vitamin D', 0)
                total_calcium += user_daily.total_nutrients.get('Calcium', 0)
                total_iron += user_daily.total_nutrients.get('Iron', 0)
                total_zinc += user_daily.total_nutrients.get('Zinc', 0)
                total_vitamin_e += user_daily.total_nutrients.get('Vitamin E', 0)
                total_vitamin_k += user_daily.total_nutrients.get('Vitamin K', 0)
                total_omega_3 += user_daily.total_nutrients.get('Omega 3', 0)
                total_omega_6 += user_daily.total_nutrients.get('Omega 6', 0)
                # Add other nutrients to accumulate totals...

        # Save the calculated totals to the appropriate fields based on the time period
        if time_period == 'last_week':
            self.last_week_calories = total_calories
            self.last_week_fat = total_fat
            self.last_week_saturated_fat = total_saturated_fat
            self.last_week_carbohydrates = total_carbohydrates
            self.last_week_sugar = total_sugar
            self.last_week_protein = total_protein
            self.last_week_cholesterol = total_cholesterol
            self.last_week_sodium = total_sodium
            self.last_week_fiber = total_fiber
            self.last_week_vitamin_c = total_vitamin_c
            self.last_week_manganese = total_manganese
            self.last_week_folate = total_folate
            self.last_week_potassium = total_potassium
            self.last_week_magnesium = total_magnesium
            self.last_week_vitamin_a = total_vitamin_a
            self.last_week_vitamin_b6 = total_vitamin_b6
            self.last_week_vitamin_b12 = total_vitamin_b12
            self.last_week_vitamin_d = total_vitamin_d
            self.last_week_calcium = total_calcium
            self.last_week_iron = total_iron
            self.last_week_zinc = total_zinc
            self.last_week_vitamin_e = total_vitamin_e
            self.last_week_vitamin_k = total_vitamin_k
            self.last_week_omega_3 = total_omega_3
            self.last_week_omega_6 = total_omega_6
            # Save other nutrient totals for last week as needed...
        elif time_period == 'last_30_days':
            self.last_30_days_calories = total_calories
            self.last_30_days_fat = total_fat
            self.last_30_days_saturated_fat = total_saturated_fat
            self.last_30_days_carbohydrates = total_carbohydrates
            self.last_30_days_sugar = total_sugar
            self.last_30_days_protein = total_protein
            self.last_30_days_cholesterol = total_cholesterol
            self.last_30_days_sodium = total_sodium
            self.last_30_days_fiber = total_fiber
            self.last_30_days_vitamin_c = total_vitamin_c
            self.last_30_days_manganese = total_manganese
            self.last_30_days_folate = total_folate
            self.last_30_days_potassium = total_potassium
            self.last_30_days_magnesium = total_magnesium
            self.last_30_days_vitamin_a = total_vitamin_a
            self.last_30_days_vitamin_b6 = total_vitamin_b6
            self.last_30_days_vitamin_b12 = total_vitamin_b12
            self.last_30_days_vitamin_d = total_vitamin_d
            self.last_30_days_calcium = total_calcium
            self.last_30_days_iron = total_iron
            self.last_30_days_zinc = total_zinc
            self.last_30_days_vitamin_e = total_vitamin_e
            self.last_30_days_vitamin_k = total_vitamin_k
            self.last_30_days_omega_3 = total_omega_3
            self.last_30_days_omega_6 = total_omega_6
            # Save other nutrient totals for last 30 days as needed...

        self.save()
