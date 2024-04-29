from django.contrib import admin
from .user_profile import UserProfile
from .allergies import Allergies
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Allergies)

