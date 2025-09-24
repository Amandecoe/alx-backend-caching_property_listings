from django.shortcuts import render
from django.views.decorators.cache import cache_page
# Create your views here.

@cache_page(60 * 15)
def property_list(request):
        properties =  Property.Objects.all().values('id','name','price','location')
        data = list(properties)
        return JsonResponse(data, safe=False)
