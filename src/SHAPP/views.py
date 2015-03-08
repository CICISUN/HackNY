from django.shortcuts import render, render_to_response, RequestContext
from django.shortcuts import render
from django.http import HttpResponse
from django.core.context_processors import request
import django.db as jdb
from pymongo import MongoClient
from mongoengine import connect
from models import Company

connect('test')

 
def insert(request):
    client = MongoClient()
    db = client.test
    f=Company()
    
    f.name='Test'
    f.phone='12345678'
    f.email='test@test.com'
    f.save(Company)
    return HttpResponse('OK!')

 
# for user_data in users.find():
#     user_list.append(user_data.getJson())
# return HttpResponse(user_list)        


# def index(request):
#      #return HttpResponse('Templates/index.html',locals(),context_instance = RequestContext(request))
#       return render(request, 'static/index.html')
# 
#  
    
 