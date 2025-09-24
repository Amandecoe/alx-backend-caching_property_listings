from django.shortcuts import render

# Create your views here.
CACHE_TTL = 60 * 15

@cache_page(CACHE_TTL)
def property_list(request):
        properties =  Property.Objects.all().values('id','name','price','location')
        data = list(properties)
        return JsonResponse(data, safe=False)
