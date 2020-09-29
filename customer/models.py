from django.db import models
from datetime import datetime

# Create your models here.

class Customer(models.Model):
    cname = models.CharField(max_length=15)
    bname = models.CharField(max_length=15)
    phone = models.IntegerField(primary_key=True,unique=True)
    email = models.EmailField(unique=True)
    dob = models.CharField(max_length=15)
    gender = models.CharField(max_length=15)
    status = models.CharField(max_length=15) 
    pan = models.CharField(max_length=15, unique=True)
    adhar = models.IntegerField(unique=True)


    def __str__(self):
        return self.cname