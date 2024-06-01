from django.contrib import admin
from .user_daily import UserDaily
from django.contrib import admin
from .food_intake import FoodIntake
from .food_intake_detail import FoodIntakeDetail

admin.site.register(FoodIntakeDetail)
admin.site.register(UserDaily)
@admin.register(FoodIntake)
class InvoiceItemAdmin(admin.ModelAdmin):
    list_display =  [field.name for field in FoodIntake._meta.fields]
