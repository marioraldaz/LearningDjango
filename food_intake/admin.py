from django.contrib import admin
from .user_daily import UserDaily
from django.contrib import admin
from .food_intake import FoodIntake
from .food_intake_detail import FoodIntakeDetail

admin.site.register(FoodIntake)
admin.site.register(FoodIntakeDetail)
admin.site.register(UserDaily)