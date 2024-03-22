from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from..user_profile import UserProfile
from..food import Food
from..food_intake import UserFoodIntake
from..allergies import Allergy
from..saved_recipes import SavedRecipe
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
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

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




class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token


class MyTokenObtainPairView(TokenObtainPairView):
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
        username = data.get('username')
        password = data.get('password')
        try:
            profile = UserProfile.objects.get(username=username)
            if check_password(password, profile.password):
                # Generate JWT token
                token = jwt.encode({'user_id': profile.id}, settings.SECRET_KEY, algorithm='HS256')
                profile_data = {field.name: getattr(profile, field.name) for field in UserProfile._meta.fields}
                profile_picture_url = profile.profile_picture.url if profile.profile_picture else None
                profile_data['profile_picture'] = profile_picture_url
                print(profile_data)
                refresh_token = jwt.encode({'user_id': profile.id}, settings.REFRESH_SECRET_KEY, algorithm='HS256')

                return JsonResponse({'success': True, 'token': token, 'refresh_token':refresh_token, 'user': profile_data})
            else:
                return JsonResponse({'success': False, 'error': 'Invalid password'})
        except UserProfile.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'User does not exist'})
    else:
        return JsonResponse({'success': False, 'error': 'Method not allowed'}, status=405)

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@require_http_methods(["POST"])
def get_profile(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        token = data.get('token')
        try:
            decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user_id = decoded_token.get('user_id')
            try:
                profile = UserProfile.objects.get(id=user_id)
                profile_data = {
                    field.name: getattr(profile, field.name) for field in UserProfile._meta.fields
                }
                profile_picture_url = profile.profile_picture.url if profile.profile_picture else None
                profile_data['profile_picture'] = profile_picture_url

                return JsonResponse({'success': True, 'user': profile_data})
            except UserProfile.DoesNotExist:
                return JsonResponse({'success': False, 'error': 'User profile not found'})
        except jwt.ExpiredSignatureError:
            return JsonResponse({'success': False, 'error': 'Expired token'}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({'success': False, 'error': 'Invalid token'}, status=401)
    else:
        return JsonResponse({'success': False, 'error': 'Method not allowed'}, status=405)
    

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


from ..forms import ProfilePictureForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

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


from ..saved_recipes import SavedRecipe
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