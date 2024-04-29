from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from profiles.user_profile import UserProfile
from food_intake.food_intake import FoodIntake
from profiles.allergies import Allergies
from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from.serializers import (
    UserProfileSerializer,
)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

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
