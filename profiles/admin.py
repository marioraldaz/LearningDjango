from django.contrib import admin
from .user_profile import UserProfile
from .allergies import Allergies
from .profile_fitness import UserFitnessProfile
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Allergies)
admin.site.register(UserFitnessProfile)
