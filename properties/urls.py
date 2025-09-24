from django.urls import path
from .views import property_list

url_patterns = [
   path('properties/', property_list, name = 'property-list'),
]