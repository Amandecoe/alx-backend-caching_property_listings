from django.shortcuts import render

# Create your views here.
CACHE_TTL = 60 * 15
class property_list(View):
    def get(self, request, *args, **kwargs):
        properties =  Property.Objects.all().values('id','name','price','location')
        data = list(properties)
        return JsonResponse(data, safe=False)
