from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..food_intake import FoodIntake
from ..food_intake_detail import FoodIntakeDetail
from .serializer import FoodIntakeSerializer, FoodIntakeDetailSerializer

@api_view(['GET', 'POST'])
def food_intake_list(request):
    if request.method == 'GET':
        food_intakes = FoodIntake.objects.all()
        serializer = FoodIntakeSerializer(food_intakes, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = FoodIntakeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def food_intake_detail(request, pk):
    try:
        food_intake = FoodIntake.objects.get(pk=pk)
    except FoodIntake.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FoodIntakeSerializer(food_intake)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FoodIntakeSerializer(food_intake, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        food_intake.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)