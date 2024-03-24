from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..food_intake import FoodIntake
from ..food_intake_detail import FoodIntakeDetail
from .serializer import FoodIntakeSerializer, FoodIntakeDetailSerializer
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
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
    
from django.http import JsonResponse
def save_food_intake(request):
    if request.method == 'POST':
        # Get data from the request's body (assuming it's sent as FormData)
        intake_data = request.POST

        # Extract relevant data for creating a FoodIntake instance
        meal_type = intake_data.get('meal_type')
        intake_date = intake_data.get('intake_date')
        profile_id = intake_data.get('profile_id')

        # Validate and create the FoodIntake instance
        try:
            food_intake = FoodIntake.objects.create(
                meal_type=meal_type,
                intake_date=intake_date,
                profile_id=profile_id
            )
            # Optionally, you can return a success message or data
            return JsonResponse({'success': True, 'message': 'Food intake saved successfully'})
        except Exception as e:
            # Handle any exceptions or validation errors
            return JsonResponse({'success': False, 'error': str(e)}, status=400)

    # If the request method is not POST, return an error
    return JsonResponse({'success': False, 'error': 'Only POST requests are allowed'}, status=405)

