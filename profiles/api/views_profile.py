from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import permission_classes
from ..forms import ProfilePictureForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from profiles.user_profile import UserProfile
from django.contrib.auth.hashers import make_password, check_password
import json
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import viewsets
from .serializers import UserProfileSerializer
from django.conf import settings
import jwt
from django.views.decorators.http import require_http_methods
from foods.recipe import Recipe


@ensure_csrf_cookie
@require_http_methods(["POST"])

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        try:
            # Extract data from request
            data = request.data

            # Validate the incoming data
            required_fields = ['username', 'password', 'email']
            for field in required_fields:
                if field not in data:
                    return JsonResponse({'error': f'Missing field: {field}'}, status=status.HTTP_400_BAD_REQUEST)

            # Extract validated data
            username = data['username']
            password = make_password(data['password'])
            email = data['email']
            gender = data.get('gender')  # Optional field
            date_of_birth = data.get('date_of_birth')  # Optional field

            # Create a new user instance
            user = UserProfile.objects.create(username=username, password=password, email=email, date_of_birth=date_of_birth)

            # Set optional fields if provided
            if gender:
                user.gender = gender
            if date_of_birth:
                user.date_of_birth = date_of_birth

            # Save the user instance
            user.save()

            return JsonResponse({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return JsonResponse({'error': 'Method Not Allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)




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
            print(request)
            return Response({'success': False, 'message': 'Invalid form data'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'success': False, 'message': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
def save_recipe(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            recipe_id = data.get('recipe_id')
            profile_id = data.get('profile_id')

            # Check if the recipe_id and profile_id are provided
            if recipe_id is None or profile_id is None:
                return Response({'error': 'Missing data'}, status=status.HTTP_400_BAD_REQUEST)

            # Get the UserProfile instance
            user_profile = UserProfile.objects.get(id=profile_id)

            # Get the Recipe instance
            recipe = Recipe.objects.get(id=recipe_id)

            # Save the recipe for the user profile
            user_profile.save_recipe(recipe)

            # Return a success response
            return Response({'message': 'Recipe saved successfully'})
        except json.JSONDecodeError:
            return Response({'error': 'Invalid JSON data'}, status=status.HTTP_400_BAD_REQUEST)
        except (UserProfile.DoesNotExist, Recipe.DoesNotExist):
            return Response({'error': 'User profile or recipe not found'}, status=status.HTTP_404_NOT_FOUND)
    else:
        # Return an error for unsupported HTTP methods
        return Response({'error': 'Method Not Allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
def get_saved_recipes(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            profile_id = data.get('profile_id')

            # Check if profile_id is provided
            if profile_id is None:
                return Response({'error': 'Missing profile_id'}, status=status.HTTP_400_BAD_REQUEST)

            # Get the UserProfile instance
            user_profile = UserProfile.objects.get(id=profile_id)

            # Get saved recipes for the user profile
            saved_recipes = user_profile.get_saved_recipes()

            # Convert queryset to list of recipe IDs for JSON response
            recipes_data = [recipe.id for recipe in saved_recipes]

            # Return the list of saved recipe IDs as JSON response
            return Response({'saved_recipes': recipes_data})
        except json.JSONDecodeError:
            return Response({'error': 'Invalid JSON data'}, status=status.HTTP_400_BAD_REQUEST)
        except UserProfile.DoesNotExist:
            return Response({'error': 'User profile not found'}, status=status.HTTP_404_NOT_FOUND)
    else:
        # Return an error for unsupported HTTP methods
        return Response({'error': 'Method Not Allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
def unsave_recipe(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            profile_id = data.get('profile_id')
            recipe_id = data.get('recipe_id')

            # Check if profile_id and recipe_id are provided
            if profile_id is None or recipe_id is None:
                return Response({'error': 'Missing data'}, status=status.HTTP_400_BAD_REQUEST)

            # Get the UserProfile instance
            user_profile = UserProfile.objects.get(id=profile_id)

            # Get the Recipe instance
            recipe = Recipe.objects.get(id=recipe_id)

            # Remove the recipe from the user profile's saved recipes
            user_profile.remove_recipe(recipe)

            # Return a success response
            return Response({'success': True, 'message': 'Recipe unsaved successfully'})
        except json.JSONDecodeError:
            return Response({'error': 'Invalid JSON data'}, status=status.HTTP_400_BAD_REQUEST)
        except (UserProfile.DoesNotExist, Recipe.DoesNotExist):
            return Response({'error': 'User profile or recipe not found'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'error': 'Method Not Allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)