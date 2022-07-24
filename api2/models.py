from unicodedata import name
from django.db import models
from numpy import roll

# Create your models here.

class studnt(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=50)
