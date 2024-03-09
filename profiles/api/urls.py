from django.urls import path, include
from rest_framework import routers
from profiles.api import views
from rest_framework.documentation import include_docs_urls
from .views import login
from django.urls import path
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
#api versioning
router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet, 'user')
router.register(r'food', views.FoodViewSet, 'food')
router.register(r'userfoodintake', views.UserFoodIntakeViewSet, 'userfoodintake')
router.register(r'allergy', views.AllergyViewSet, 'allergy')
router.register(r'savedrecipe', views.SavedRecipeViewSet, 'savedrecipe')
router.register(r'userrecipe', views.UserRecipeViewSet, 'userrecipe')
urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("docs/", login, name='login'),
    path('', views.get_routes),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', views.get_profile),

]


