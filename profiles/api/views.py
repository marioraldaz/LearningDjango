from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from..user_profile import UserProfile
from..food import Food
from..food_intake import UserFoodIntake
from..allergies import Allergy
from..savedRecipe import SavedRecipe
from..user_recipe import UserRecipe
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from..forms import LoginForm
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from.serializer import (
    UserSerializer,
    FoodSerializer,
    UserFoodIntakeSerializer,
    AllergySerializer,
    SavedRecipeSerializer,
    UserRecipeSerializer
)
import json
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import status
from django.contrib.auth.decorators import login_required


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # Validate the incoming data

        # Extract validated data
        username = serializer.validated_data['username']
        password = make_password(serializer.validated_data['password'])
        email = serializer.validated_data['email']
        gender = serializer.validated_data.get('gender')
        weight = serializer.validated_data.get('weight')
        height = serializer.validated_data.get('height')
        date_of_birth = serializer.validated_data.get('date_of_birth')

        # Create a new user instance without gender and date_of_birth
        user = UserProfile.objects.create(username=username, password=password, email=email, gender=gender, date_of_birth=date_of_birth)

        # Save the user instance
        user.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


@ensure_csrf_cookie
@require_http_methods(["POST"])
def login(request):
    data = request.body.decode('utf-8')

    # Get username and password from the request body (assuming it's a JSON object)
    data = json.loads(data)

    username = data.get('username')
    password = data.get('password')

    # Retrieve the user from the database based on the provided username
    try:
        user = UserProfile.objects.get(username=username)
    except UserProfile.DoesNotExist:
        user = None

    # Check if the user exists and the password is correct
    if user is not None and check_password(password, user.password):
        # If authentication succeeds, set user session and return success response
        request.session['user_id'] = user.id
        return JsonResponse({'success': True, 'message': 'Login successful'})
    else:
        # If authentication fails, return error response
        return JsonResponse({'success': False, 'message': 'Invalid username or password'}, status=400)


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class UserFoodIntakeViewSet(viewsets.ModelViewSet):
    queryset = UserFoodIntake.objects.all()
    serializer_class = UserFoodIntakeSerializer


class AllergyViewSet(viewsets.ModelViewSet):
    queryset = Allergy.objects.all()
    serializer_class = AllergySerializer


class SavedRecipeViewSet(viewsets.ModelViewSet):
    queryset = SavedRecipe.objects.all()
    serializer_class = SavedRecipeSerializer


class UserRecipeViewSet(viewsets.ModelViewSet):
    queryset = UserRecipe.objects.all()
    serializer_class = UserRecipeSerializer


@api_view(['GET'])
def get_routes(request):
    routes = [
        '/api/token',
        '/api/token/refresh'
    ]
    return JsonResponse(routes, safe=False)


@api_view(['GET'])
@login_required
def get_profile(request):
    print("profile::::::",profile)
    user = request.user
    profile = user.profile
    serializer = UserSerializer(profile, many=False)
    return Response(serializer.data)

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        print("lololo")
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    print("lalalal")
    serializer_class = MyTokenObtainPairSerializer
    
from django.conf import settings
import jwt


from django.views.decorators.csrf import csrf_protect

@ensure_csrf_cookie
@require_http_methods(["POST"])
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        data = json.loads(request.body.decode('utf-8'))
        print(data)
        username = data.get('username')
        password = data.get('password')
        try:
            profile = UserProfile.objects.get(username=username)
            if check_password(password, profile.password):
                # Generate JWT token
                token = jwt.encode({'user_id': profile.id}, settings.SECRET_KEY, algorithm='HS256')
                return JsonResponse({'success': True, 'token': token})
            else:
                return JsonResponse({'success': False, 'error': 'Invalid password'})
        except UserProfile.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'User does not exist'})
    else:
        return JsonResponse({'success': False, 'error': 'Method not allowed'}, status=405)
