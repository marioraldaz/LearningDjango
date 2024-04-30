from django.urls import path
from rest_framework import routers
from profiles.api import views
from .views import *
from .views_profile import *
from .views_user_fitness_profile import FitnessProfileView

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet, 'user')


urlpatterns = [
    path('token/refresh/', refresh_token, name='token_refresh'),
    path("register/", register, name='register'),
    path("login/", login, name='login'),
    path("get_profile/", get_profile, name='get_profile'),
    path('upload-profile-picture/', upload_profile_picture, name='upload_profile_picture'),
    path('save-recipe', save_recipe, name="save_recipe"),
    path('get-saved-recipes', get_saved_recipes, name="get_saved_recipes"),
    path('unsave-recipe', unsave_recipe, name="unsave_recipe"),
    path('change-password/', change_password, name='change_password'),
    path('fitness_profile/', FitnessProfileView.as_view(), name='fitness_profile'),
]


from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
