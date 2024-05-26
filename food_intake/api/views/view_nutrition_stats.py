from datetime import date, timedelta
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from food_intake.user_daily import UserDaily
from ...models import NutritionStats
from ..serializers import NutritionStatsSerializer
from django.core.serializers import serialize



class NutritionStatsView(APIView):
    def get(self, request, profile_id, format=None):
        try:
            nutrition_stats = NutritionStats.objects.get(profile_id=profile_id)
            stats = NutritionStatsSerializer(nutrition_stats).data
            end_date = date.today()
            start_date_last_week = end_date - timedelta(days=7)
            start_date_last_month = end_date - timedelta(days=30)

            # Get UserDaily objects for the last week and last month
            last_week_objects = UserDaily.objects.filter(date__range=[start_date_last_week, end_date])
            last_month_objects = UserDaily.objects.filter(date__range=[start_date_last_month, end_date])

            # Serialize the data if needed
            last_week_data = serialize('json', last_week_objects)
            last_month_data = serialize('json', last_month_objects)
            last_week_data = json.loads(last_week_data)
            last_month_data = json.loads(last_month_data)
            # You can customize the response format as needed
            response_data = {
                'last_week': last_week_data,
                'last_month': last_month_data,
                'stats': stats
            }

            return Response(response_data, status=status.HTTP_200_OK)
        except NutritionStats.DoesNotExist:
            return Response({"error": "NutritionStats not found for this profile"}, status=status.HTTP_404_NOT_FOUND)
        
   