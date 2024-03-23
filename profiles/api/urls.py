from django.urls import path, include
from rest_framework import routers
from profiles.api import views
from rest_framework.documentation import include_docs_urls
from .views import *
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("docs/", include_docs_urls(title="User API")),
    path('', views.get_routes),
    path('token/refresh/', refresh_token, name='token_refresh'),
    path('profile/', views.get_profile),
    path("login/", login, name='login'),
    path("get_profile/", get_profile, name='login'),
    path('upload-profile-picture/', upload_profile_picture, name='upload_profile_picture'),
    path('save-recipe', save_recipe, name="save_recipe"),
    path('get-saved-recipes', get_saved_recipes, name="get_saved_recipes"),
    path('unsave-recipe', unsave_recipe, name="unsave_recipe"),
    path('food-intake/', food_intake_list, name='food_intake_list'),
    path('food-intake/<int:pk>/', food_intake_detail, name='food_intake_detail'),
]


from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
