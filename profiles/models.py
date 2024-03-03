from django.db import models
# Create your models here.


class Profile(models.Model):
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    gender = models.CharField(max_length=10, choices=(('Male', 'Male'), ('Female', 'Female')))
    email = models.EmailField(max_length=50)
    weight = models.IntegerField(default=80)
    height = models.IntegerField(default=170)
    date_of_birth = models.DateField()
    def __str__(self):
        return self.username