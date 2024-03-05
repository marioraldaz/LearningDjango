from django.db import models
from django.core.validators import MinLengthValidator

class User(models.Model):
    username = models.CharField(max_length=25, validators=[MinLengthValidator(6)])
    password = models.CharField(max_length=25, validators=[MinLengthValidator(6)])
    gender = models.CharField(max_length=10, choices=(('Male', 'Male'), ('Female', 'Female')))
    email = models.EmailField(max_length=50)
    weight = models.IntegerField(default=80)
    height = models.IntegerField(default=170)
    date_of_birth = models.DateField()
    def __str__(self):
        return self.username