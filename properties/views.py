from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from .utils import get_all_properties
# Create your views here.

@cache_page(60 * 15)
def property_list(request):
        data = get_all_properties
        return JsonResponse({"data":data})
