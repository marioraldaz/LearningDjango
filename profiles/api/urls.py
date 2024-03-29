from django.urls import path, include
from rest_framework import routers
from profiles.api import views
from rest_framework.documentation import include_docs_urls
from .views import *
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
#api versioning
router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet, 'user')
router.register(r'food', views.FoodViewSet, 'food')
router.register(r'foodintake', views.FoodIntakeViewSet, 'foodintake')
router.register(r'allergy', views.AllergyViewSet, 'allergy')
router.register(r'savedrecipe', views.SavedRecipeViewSet, 'savedrecipe')
router.register(r'userrecipe', views.UserRecipeViewSet, 'userrecipe')

urlpatterns = [
    path("api/v1/", include(router.urls)),
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
    path('change-password/', change_password, name='change_password'),
]


from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
