from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from food_intake.user_daily import UserDaily
from food_intake.food_intake import FoodIntake
from food_intake.food_intake_detail import FoodIntakeDetail
from food_intake.api.serializers import UserDailySerializer, FoodIntakeSerializer, FoodIntakeDetailSerializer

class UserDailyView(APIView):
    def get(self, request, profile_id):
        user_dailies = UserDaily.objects.filter(profile_id=profile_id)
        serializer = UserDailySerializer(user_dailies, many=True)
        return Response(serializer.data)

    def post(self, request, profile_id):
        request.data['profile'] = profile_id  # Set the profile_id in the request data
        serializer = UserDailySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, profile_id, pk):
        try:
            user_daily = UserDaily.objects.get(profile_id=profile_id, pk=pk)
        except UserDaily.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        user_daily.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def list_food_intakes(self):
        food_intakes = FoodIntake.objects.all()
        serializer = FoodIntakeSerializer(food_intakes, many=True)
        return Response(serializer.data)

    def list_food_intakes_with_details(self):
        food_intakes = FoodIntake.objects.all()
        data = []
        for food_intake in food_intakes:
            intake_details = FoodIntakeDetail.objects.filter(food_intake=food_intake)
            intake_data = {
                'food_intake': FoodIntakeSerializer(food_intake).data,
                'details': FoodIntakeDetailSerializer(intake_details, many=True).data
            }
            data.append(intake_data)
        return Response(data)