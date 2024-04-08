from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from food_intake.food_intake import FoodIntake
from ..serializers import FoodIntakeSerializer
from food_intake.food_intake_detail import FoodIntakeDetail
from ..serializers import FoodIntakeSerializer, FoodIntakeDetailSerializer
from rest_framework.exceptions import NotFound

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
        serializer = FoodIntakeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
            raise NotFound("Food Intake not found")