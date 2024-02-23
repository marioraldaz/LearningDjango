from django.db import models
from django.contrib.auth import get_user_model
from datetime import date

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    done = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    
class Client(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    age = models.IntegerField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.title

class ProteinIntake(models.Model):
    user = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    protein_consumed = models.FloatField(default=0.0)
    
    