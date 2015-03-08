from django.shortcuts import render, render_to_response, RequestContext
from django.shortcuts import render
from django.http import HttpResponse
from django.core.context_processors import request
import django.db as jdb
from pymongo import MongoClient
from mongoengine import connect

connect('test')


# def index(request):
#      #return HttpResponse('Templates/index.html',locals(),context_instance = RequestContext(request))
#       return render(request, 'static/index.html')
# 
#  
    
 