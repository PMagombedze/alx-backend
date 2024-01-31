#!/usr/bin/env python3


"""
Basic dictionary
"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    A basic cache class

    Attributes:
        MAX_ITEMS: number of items that can be store in the cache
    """
    def put(self, key, item):
        """put in dictionary"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """get key"""
        if key is not None and key in self.cache_data:
            return self.cache_data.get(key)
        else:
            return None
