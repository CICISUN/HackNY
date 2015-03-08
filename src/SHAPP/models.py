from django.db import models
import pymongo
from mongoengine import *
import mongoengine

connect('test') 


class Company(mongoengine.Document):    
    name = mongoengine.StringField()
    email = mongoengine.EmailField()
    phone = mongoengine.StringField()
    pic = mongoengine.StringField()
    lat = mongoengine.FloatField()
    lon = mongoengine.FloatField()
    description = mongoengine.StringField()
    Founded_Time = mongoengine.StringField()
    kwd = mongoengine.StringField(max_length=50)
    Company_URL = mongoengine.StringField()
       