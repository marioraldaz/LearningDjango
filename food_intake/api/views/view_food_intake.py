from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from food_intake.food_intake import FoodIntake
from ..serializers import FoodIntakeSerializer
from food_intake.food_intake_detail import FoodIntakeDetail
from ..serializers import FoodIntakeSerializer, FoodIntakeDetailSerializer
from rest_framework.exceptions import NotFound
from django.http import Http404
from rest_framework.exceptions import ValidationError
from django.db import transaction


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
        # Deserialize the request data manually
        data = request.data

        # Extract the main attributes for FoodIntake creation
        profile_id = data.get('profile_id')
        meal_type = data.get('meal_type')
        date = data.get('date')
        details_data = data.get('details', [])

        try:
            with transaction.atomic():  # Use transaction to ensure atomicity of database operations
                # Create the FoodIntake object
                food_intake = FoodIntake.objects.create(profile_id=profile_id, meal_type=meal_type, date=date)

                # Create FoodIntakeDetail instances and associate them with the FoodIntake
                details_instances = []
                for detail_data in details_data:
                    content_type = detail_data.get('content_type')
                    food_id = detail_data.get('food_id')
                    amount = detail_data.get('amount')
                    detail_instance = FoodIntakeDetail.objects.create(food_intake=food_intake, content_type=content_type, food_id=food_id, amount=amount)
                    details_instances.append(detail_instance)

                # Build the response data manually
                response_data = {
                    'id': food_intake.id,
                    'profile_id': food_intake.profile_id,
                    'meal_type': food_intake.meal_type,
                    'date': food_intake.date,
                    'details': [
                        {
                            'id': detail.id,
                            'content_type': detail.content_type,
                            'food_id': detail.food_id,
                            'amount': detail.amount
                        }
                        for detail in details_instances
                    ]
                }

                # Return a successful response with the manually constructed response data
                return Response(response_data, status=status.HTTP_201_CREATED)

        except Exception as e:
            # If any exception occurs during processing, handle it gracefully
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

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