from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from..user_profile import UserProfile
from..food import Food
from..food_intake import FoodIntake
from..allergies import Allergy
from..saved_recipes import SavedRecipe
from..user_recipe import UserRecipe
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from.serializer import (
    UserSerializer,
    FoodSerializer,
    FoodIntakeSerializer,
    AllergySerializer,
    SavedRecipeSerializer,
    UserRecipeSerializer
)
from ..forms import ProfilePictureForm
from rest_framework.decorators import api_view
from ..saved_recipes import SavedRecipe
from rest_framework.response import Response
from rest_framework import status
import json
from django.http import JsonResponse
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .views_food_intake import *
from rest_framework.views import APIView
from django.conf import settings
import jwt

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



class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class FoodIntakeViewSet(viewsets.ModelViewSet):
    queryset = FoodIntake.objects.all()
    serializer_class = FoodIntakeSerializer


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




class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    
class UserProfileView(APIView):
    def post(self, request, *args, **kwargs):
        if 'username' in request.data and 'password' in request.data:
            username = request.data['username']
            password = request.data['password']
            user = authenticate(username=username, password=password)
            if user:
                token = jwt.encode({'user_id': user.id}, settings.SECRET_KEY, algorithm='HS256')
                profile_data = {
                    field.name: getattr(user, field.name) for field in user._meta.fields
                }
                profile_picture_url = user.profile_picture.url if user.profile_picture else None
                profile_data['profile_picture'] = profile_picture_url
                refresh_token = jwt.encode({'user_id': user.id}, settings.REFRESH_SECRET_KEY, algorithm='HS256')
                return Response({'success': True, 'token': token, 'refresh_token': refresh_token, 'user': profile_data})
            else:
                return Response({'success': False, 'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'success': False, 'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        token = request.data.get('token')
        if token:
            try:
                decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
                user_id = decoded_token.get('user_id')
                try:
                    user = UserProfile.objects.get(id=user_id)
                    profile_data = {
                        field.name: getattr(user, field.name) for field in user._meta.fields
                    }
                    profile_picture_url = user.profile_picture.url if user.profile_picture else None
                    profile_data['profile_picture'] = profile_picture_url
                    return Response({'success': True, 'user': profile_data})
                except UserProfile.DoesNotExist:
                    return Response({'success': False, 'error': 'User profile not found'}, status=status.HTTP_404_NOT_FOUND)
            except jwt.ExpiredSignatureError:
                return Response({'success': False, 'error': 'Expired token'}, status=status.HTTP_401_UNAUTHORIZED)
            except jwt.InvalidTokenError:
                return Response({'success': False, 'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'success': False, 'error': 'Token is required'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def upload_profile_picture(request):
    if request.method == 'POST':
        form = ProfilePictureForm(request.data, request.FILES)
        if form.is_valid():
            profile_id = request.data.get('profile_id')
            try:
                profile = UserProfile.objects.get(id=profile_id)
            except UserProfile.DoesNotExist:
                return Response({'success': False, 'message': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)

            # Check if profile already has a profile picture
            if profile.profile_picture:
                # Delete the previous profile picture from storage and database
                profile.profile_picture.delete()

            # Save the new profile picture
            profile.profile_picture = request.FILES['profile_picture']
            profile.save()
            return Response({'success': True, 'message': 'Profile picture uploaded successfully'})
        else:
            return Response({'success': False, 'message': 'Invalid form data'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'success': False, 'message': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@require_http_methods(["POST"])
def refresh_token(request):
    try:
        refresh_token = request.data.get('refresh')
        if not refresh_token:
            return Response({'error': 'Refresh token is required'}, status=status.HTTP_400_BAD_REQUEST)

        refresh = RefreshToken(refresh_token)
        access_token = str(refresh.access_token)
        return Response({'access': access_token}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['POST'])

def save_recipe(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            recipe_id = data.get('recipe_id')
            profile_id = data.get('profile_id')

            # Check if the recipe_id and profile_id are provided
            if recipe_id is None or profile_id is None:
                return JsonResponse({'error': 'Missing data'}, status=400)

            # Check if the recipe_id already exists
            if SavedRecipe.objects.filter(recipe_id=recipe_id).exists():
                return JsonResponse({'error': 'Recipe already saved'}, status=400)

            # Save the recipe data into the SavedRecipe model
            SavedRecipe.objects.create(recipe_id=recipe_id, profile_id=profile_id)

            # Return a success response
            return JsonResponse({'message': 'Recipe saved successfully'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    else:
        # Return an error for unsupported HTTP methods
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)

def get_saved_recipes(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            profile_id = data.get('profile_id')

            # Check if profile_id is provided
            if profile_id is None:
                return JsonResponse({'error': 'Missing profile_id'}, status=400)

            # Query SavedRecipe model to get saved recipes for the profile_id
            saved_recipes = SavedRecipe.objects.filter(profile_id=profile_id)

            # Convert queryset to list of dictionaries for JSON response
            recipes_data = [recipe.recipe_id for recipe in saved_recipes]

            # Return the list of saved recipes as JSON response
            return JsonResponse({'saved_recipes': recipes_data})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    else:
        # Return an error for unsupported HTTP methods
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)
    
def unsave_recipe(request):
    if request.method == 'POST':
        try:
            profile_id = request.POST.get('profile_id')
            recipe_id = request.POST.get('recipe_id')

            # Check if profile_id and recipe_id are provided
            if profile_id is None or recipe_id is None:
                return JsonResponse({'error': 'Missing data'}, status=400)

            # Find the saved recipe entry and delete it
            saved_recipe = SavedRecipe.objects.filter(profile_id=profile_id, recipe_id=recipe_id).first()
            if saved_recipe:
                saved_recipe.delete()
                return JsonResponse({'success': True, 'message': 'Recipe unsaved successfully'})
            else:
                return JsonResponse({'error': 'Saved recipe not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Method Not Allowed'}, status=405)


def change_password(request):
    if request.method == 'POST':
        user_id = request.POST.get('id') 
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')

        try:
            user_profile = UserProfile.objects.get(pk=user_id)
            print(old_password)
        except UserProfile.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'User profile not found.'}, status=400)

        # Check if old password matches the current user's password
        if check_password(old_password, user_profile.password):
            # Hash the new password
            hashed_password = make_password(new_password)

            # Update user's password
            user_profile.password = hashed_password
            user_profile.save()

            return JsonResponse({'success': True, 'message': 'Password changed successfully.'})
        else:
            return JsonResponse({'success': False, 'message': 'Incorrect old password.'}, status=400)

    return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=400)
