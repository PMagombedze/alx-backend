#!/usr/bin/env python3


"""
Basic dictionary
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    def put(self, key, item):
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        if key is not None and key in self.cache_data:
            return self.cache_data.get(key)
        else:
            return None
