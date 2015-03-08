from tastypie.resources import ModelResource
from tastypie import authorization
from tastypie_mongoengine import resources
from SHAPP.models import Company
from tastypie.constants import ALL
from pymongo import MongoClient
from mongoengine import connect

class EntryResource(resources.MongoEngineResource):
    class Meta:
        queryset = Company.objects.all()  
        authorization = authorization.Authorization()  
        resource_name = 'company'
#         filtering = {'kwd': ALL}


 
 
 
        