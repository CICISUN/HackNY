from django.db import models
import pymongo
from mongoengine import *

connect('test') 



class Business(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()