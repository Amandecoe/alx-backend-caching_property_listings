from django.core.cache import cache
from .models import Property  

CACHE_KEY = 'all_properties'
CACHE_TTL = 3600 #Seconds in an hour
def get_all_properties():
    properties = cache.get(CACHE_KEY)
    if properties is not None:
        return properties
    #if not in cache, fetch from database
    properties =  list(Property.objects.all().values('title', 'location', 'price'))    

    #store it in redis cache for one hour
    cache.set(CACHE_KEY, properties, CACHE_TTL)
    return properties