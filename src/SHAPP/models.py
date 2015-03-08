from django.db import models
import pymongo
from mongoengine import *

connect('test') 


class Company(models.Model):    
    name = StringField()
    email = EmailField()
    phone = StringField()
    pic = StringField()
    lat = models.FloatField()
    lon = models.FloatField()
    description = models.TextField()
    Founded_Time = models.DateField()
    kwd = models.CharField(max_length=50)
    Company_URL = StringField()
      