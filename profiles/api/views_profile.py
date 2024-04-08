from rest_framework.views import APIView
from django.contrib.auth import authenticate
from ..forms import ProfilePictureForm
from rest_framework.response import Response
from rest_framework import status
import jwt
from django.conf import settings
from..user_profile import UserProfile


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


