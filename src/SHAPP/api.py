from tastypie.resources import ModelResource
from SHAPP.models import Company
from tastypie.constants import ALL

class EntryResource(ModelResource):
    class Meta:
        limit = 0
        queryset = Company.objects.all()  
        print queryset    
        resource_name = 'company'
#         filtering = {'kwd': ALL}
       