from django.core.cache import cache
from .models import Property  
import logging

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
logger = logging.getLogger(__name__)

def get_redis_cache_metrics():
    """
    Fetch Redis cache metrics: hits, misses, and hit ratio.
    Logs and returns a dictionary with the values.
    """
    try:
        # Get the raw Redis client from django-redis
        redis_client = cache.client.get_client(write=True)

        # Get INFO stats from Redis
        info = redis_client.info()

        # Extract keyspace hits and misses
        hits = info.get('keyspace_hits', 0)
        misses = info.get('keyspace_misses', 0)

        # Calculate hit ratio safely
        total = hits + misses
        hit_ratio = hits / total if total > 0 else 0.0

        # Log metrics
        logger.info(f"Redis cache metrics: hits={hits}, misses={misses}, hit_ratio={hit_ratio:.2f}")

        # Return metrics as dictionary
        return {
            "hits": hits,
            "misses": misses,
            "hit_ratio": hit_ratio
        }

    except Exception as e:
        logger.error(f"Error fetching Redis metrics: {e}")
        return {
            "hits": 0,
            "misses": 0,
            "hit_ratio": 0.0
        }