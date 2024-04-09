from django.contrib import admin
from .user_profile import UserProfile
from .allergies import Allergy
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Allergy)

