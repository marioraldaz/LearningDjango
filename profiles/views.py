from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializer import UserSerializer
from .user import User
from .food import Food
from .food_intake import UserFoodIntake
from .allergies import Allergy
from .savedRecipe import SavedRecipe
from .user_recipe import UserRecipe


from .serializer import (
    UserSerializer,
    FoodSerializer,
    UserFoodIntakeSerializer,
    AllergySerializer,
    SavedRecipeSerializer,
    UserRecipeSerializer
)

from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializer import UserSerializer
from django.contrib.auth.hashers import make_password, check_password
from rest_framework import viewsets, status
from rest_framework.response import Response
from .user import User
from .serializer import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
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
        user = User.objects.create(username=username, password=password, email=email,gender=gender,date_of_birth=date_of_birth)
    
        
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

