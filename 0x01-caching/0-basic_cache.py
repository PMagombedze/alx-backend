#!/usr/bin/env python3


"""
Basic dictionary
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """basic cache"""
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
