from django.contrib import admin
from django.conf.urls import patterns, include, url
from SHAPP import views
 
urlpatterns = patterns('',
    
    url(r'^admin/', include(admin.site.urls)),
  
    )

urlpatterns += patterns(
    'django.contrib.staticfiles.views',
    url(r'^(?:index.html)?$', 'serve', kwargs={'path': 'index.html'}),
    url(r'^(?P<path>(?:js|css|img)/.*)$', 'serve'),
)