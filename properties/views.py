from django.shortcuts import render

# Create your views here.

@cache_page(60 * 15)
def property_list(request):
        properties =  Property.Objects.all().values('id','name','price','location')
        data = list(properties)
        return JsonResponse(data, safe=False)
