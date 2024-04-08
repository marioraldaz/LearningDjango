from rest_framework import status
from rest_framework.response import Response
from food_intake.food_intake_detail import FoodIntakeDetail
from ..serializers import FoodIntakeDetailSerializer
from rest_framework.views import APIView
from django.http import Http404


class FoodIntakeDetailView(APIView):
    def get_object(self, pk):
        try:
            return FoodIntakeDetail.objects.get(pk=pk)
        except FoodIntakeDetail.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        food_intake_detail = self.get_object(pk)
        serializer = FoodIntakeDetailSerializer(food_intake_detail)
        return Response(serializer.data)

    def put(self, request, pk):
        food_intake_detail = self.get_object(pk)
        serializer = FoodIntakeDetailSerializer(food_intake_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)