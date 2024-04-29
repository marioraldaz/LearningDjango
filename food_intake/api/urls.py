from django.urls import path
from .views.view_food_intake import FoodIntakeView
from .views.view_food_intake_detail import FoodIntakeDetailView
from .views.view_user_daily import UserDailyView

urlpatterns = [
    path('food-intake/', FoodIntakeView.as_view(), name='food_intake_list'),
    path('food-intake/<int:pk>/', FoodIntakeDetailView.as_view(), name='food_intake_detail'),
    path('food-intake/<int:pk>/details/', FoodIntakeDetailView.as_view(), name='food_intake_details'),
    path('user-dailies/<int:profile_id>/', UserDailyView.as_view(), name='user_dailies'),
    path('user-dailies/<int:profile_id>/<int:pk>/', UserDailyView.as_view(), name='user_daily_detail'),
    path('user-daily/list-food-intakes/', UserDailyView.as_view(), name='list_food_intakes'),
    path('user-daily/list-food-intakes-with-details/', UserDailyView.as_view(), name='list_food_intakes_with_details'),
]
