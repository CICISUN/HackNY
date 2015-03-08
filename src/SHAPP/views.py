from django.shortcuts import render, render_to_response, RequestContext
from django.shortcuts import render
from django.http import HttpResponse
from django.core.context_processors import request
import django.db as jdb
from pymongo import MongoClient
from mongoengine import connect
from models import Company
from curses.ascii import NUL

# connect('test')

 
def insert(request):
#     client = MongoClient()
#     db = client.test
#     f=Company()
#     f.name="Harlem Biospace",
#     f.email="hello@harlembiospace.com",
#     f.phone= "267-702-3051",
#     f.pic= "http://infinitymassagechairs.com/img/company-bg.jpg",
#     f.lat= 40.813580,
#     f.lon= -73.954203,
#     f.description= "Harlem Biospace (Hb) is a new biotech incubator, the first of its kind in New York City, to offer affordable shared wet-lab space for competitively-selected entrants",
#     f.Founded_Time= "15-02-2014",
#     f.kwd= "biotech",
#     f.Company_URL= "http://harlembiospace.com/"
#     f.save(Company)
   client = MongoClient()
   db = client.test
   company=[]
   for each in db.company.find():
       company.append(each)
       print each
   print "haha"
   return HttpResponse('OK!')

 
# for user_data in users.find():
#     user_list.append(user_data.getJson())
# return HttpResponse(user_list)        


# def index(request):
#      #return HttpResponse('Templates/index.html',locals(),context_instance = RequestContext(request))
#       return render(request, 'static/index.html')
# 
#  
    
 