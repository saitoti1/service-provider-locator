from django.core.cache import cache
from django.conf import settings


class CacheError(Exception):
    """
    Custom Cache Error
    """
    pass


class CacheService:
    """
    Set,Get and Delete cache variables
    """

    @staticmethod
    def set(name, value, expire=settings.MAX_CACHE_EXPIRE_TIME):
        """
        params:
        name: cache variable name
        value: variable value to store in cache
        expire: variable cache expire time, if not passed, set max expire time to variable cache.
        """
        try:
            cache.set(name, value, timeout=expire)
        except Exception as e:
            raise CacheError('Encountered an error when setting cache') from e

    @staticmethod
    def get(name, default=None):
        """
        params:
        name: cache variable name
        default: returns default value on get
        """
        if not default:
            default = {}
        try:
            data = cache.get(name, default)
        except Exception as e:
            raise CacheError('Encountered an error when getting from cache') from e
        return data

    @staticmethod
    def delete(name):
        """
        params:
        name: cache variable name
        """
        try:
            cache.delete(name)
        except Exception as e:
            raise CacheError('Encountered an error when deleting cache') from e
