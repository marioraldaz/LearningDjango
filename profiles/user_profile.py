from django.db import models
from django.core.validators import MinLengthValidator

class UserProfile(models.Model):
   
    username = models.CharField(max_length=25, unique=True, validators=[MinLengthValidator(6)])
    password = models.CharField(max_length=25, validators=[MinLengthValidator(6)])
    gender = models.CharField(max_length=10, choices=(('Male', 'Male'), ('Female', 'Female')))
    email = models.EmailField(max_length=50, unique=True, )
    weight = models.IntegerField(default=80)
    height = models.IntegerField(default=170)
    date_of_birth = models.DateField()
    
    activityLevel = models.PositiveIntegerField(default=1)  # Adjust the field type and default value as needed

    
    def __str__(self):
        return self.username