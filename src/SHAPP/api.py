'''
Created on Mar 7, 2015

@author: CC
'''
from tastypie.resources import ModelResource
from SHAPP.models import Tweet
from tastypie.constants import ALL

class EntryResource(ModelResource):
    class Meta:
        limit = 0
        queryset = Tweet.objects.all()
        filtering = {'kwd': ALL}
        resource_name = 'tweet'