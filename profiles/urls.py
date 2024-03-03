from django.urls import path, include
from rest_framework import routers
from profiles import views
#api versioning

router = routers.DefaultRouter()
router.register(r'profiles', views.ProfileView, 'profiles')
urlpatterns = [
    path("api/v1/", include(router.urls))
]
 