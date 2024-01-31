#!/usr/bin/env python3

"""
FIFO Cache
"""

from threading import RLock
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFO cache"""
    def __init__(self):
        """Instantiation method"""
        super().__init__()
        self.__keys = []
        self.__rlock = RLock()

    def put(self, key, item):
        """Add an item"""
        if key is not None and item is not None:
            with self.__rlock:
                discarded_key = self._balance(key)
                self.cache_data[key] = item
                if discarded_key is not None:
                    print('DISCARD: {}'.format(discarded_key))

    def get(self, key):
        """Get an item by key"""
        return self.cache_data.get(key)

    def _balance(self, keyIn):
        """Removes the oldest item"""
        discarded_key = None
        with self.__rlock:
            if keyIn not in self.__keys:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    discarded_key = self.__keys.pop(0)
                    del self.cache_data[discarded_key]
                self.__keys.append(keyIn)
        return discarded_key
