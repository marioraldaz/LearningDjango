from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ...models import NutritionStats
from ..serializers import NutritionStatsSerializer

class NutritionStatsView(APIView):
    def get(self, request, profile_id, format=None):
        try:
            nutrition_stats = NutritionStats.objects.get(profile_id=profile_id)
            serializer = NutritionStatsSerializer(nutrition_stats)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except NutritionStats.DoesNotExist:
            return Response({"error": "NutritionStats not found for this profile"}, status=status.HTTP_404_NOT_FOUND)