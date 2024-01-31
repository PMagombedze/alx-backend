#!/usr/bin/env python3

"""
Basic dictionary
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    A basic cache class
    """

    def put(self, key, item):
        """Put item in the cache using key"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Get item from the cache using key"""
        return None if key is None else self.cache_data.get(key)
