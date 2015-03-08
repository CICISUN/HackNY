from django.contrib import admin
from django.conf.urls import patterns, include, url
from SHAPP import views
from SHAPP.api import EntryResource

entry_resource = EntryResource()
 
urlpatterns = patterns('',
    
    url(r'^admin/', include(admin.site.urls)),
    url('^test/$', 'SHAPP.views.insert', name='insert'),
    url(r'^api/', include(entry_resource.urls)),
    )
# 
# urlpatterns = patterns('',
#     (r'^api/', include(v1_api.urls)),
# )

urlpatterns += patterns(
    'django.contrib.staticfiles.views',
    url(r'^(?:index.html)?$', 'serve', kwargs={'path': 'index2.html'}),
    url(r'^(?P<path>(?:js|css|img)/.*)$', 'serve'),
)