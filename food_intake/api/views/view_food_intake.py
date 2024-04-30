from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from food_intake.food_intake import FoodIntake
from ..serializers import FoodIntakeSerializer
from food_intake.food_intake_detail import FoodIntakeDetail
from ..serializers import FoodIntakeSerializer, FoodIntakeDetailSerializer
from rest_framework.exceptions import NotFound
from django.http import Http404


"""_summary_
{
    "profile": 1, 
    "meal_type": "Breakfast",
    "date": "2024-04-30",
    "details": [
    {
        "content_type": "ingredient",  // ContentType name (e.g., "ingredient" or "recipe")
        "food_id": 1,  // ID of the food item (e.g., Ingredient or Recipe ID)
        "amount": 150  // Amount consumed
    },
    {
        "content_type": "recipe",
        "food_id": 2,
        "amount": 200
    }
]
}
"""

class FoodIntakeView(APIView):
    def get(self, request):
        user_profile_id = request.GET.get('user_profile_id')
        if user_profile_id:
            food_intakes = FoodIntake.objects.filter(profile_id=user_profile_id)
        else:
            food_intakes = FoodIntake.objects.all()
        serializer = FoodIntakeSerializer(food_intakes, many=True)
        return Response(serializer.data)

    def post(self, request):
        food_intake_serializer = FoodIntakeSerializer(data=request.data)
        if food_intake_serializer.is_valid():
            food_intake = food_intake_serializer.save()
            details_data = request.data.get('details', [])
            detail_serializer = FoodIntakeDetailSerializer(data=details_data, many=True, context={'food_intake': food_intake})
            if detail_serializer.is_valid():
                detail_serializer.save()
                return Response(food_intake_serializer.data, status=status.HTTP_201_CREATED)
            food_intake.delete()  # Rollback if detail_serializer fails
        return Response(food_intake_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        try:
            food_intake = FoodIntake.objects.get(pk=pk)
            food_intake.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except FoodIntake.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get_food_intake_details(self, food_intake_id):
        try:
            food_intake = FoodIntake.objects.get(pk=food_intake_id)
            food_intake_details = FoodIntakeDetail.objects.filter(food_intake=food_intake)
            serializer = FoodIntakeDetailSerializer(food_intake_details, many=True)
            return serializer.data
        except FoodIntake.DoesNotExist:
            raise Http404("Food Intake not found")