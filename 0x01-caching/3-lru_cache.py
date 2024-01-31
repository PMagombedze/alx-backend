#!/usr/bin/env python3

"""
LRU Cache
"""

from threading import RLock
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRU Cache class"""
    def __init__(self):
        """Initialize"""
        super().__init__()
        self.__keys = []
        self.__rlock = RLock()

    def put(self, key, item):
        """Add an item in the cache"""
        if key and item:
            discarded_key = self._balance(key)
            with self.__rlock:
                self.cache_data[key] = item
            if discarded_key:
                print(f'DISCARD: {discarded_key}')

    def get(self, key):
        """Get an item from the cache"""
        with self.__rlock:
            value = self.cache_data.get(key)
            if key in self.__keys:
                self._balance(key)
        return value

    def _balance(self, key):
        """Balance the cache"""
        discarded_key = None
        with self.__rlock:
            if key not in self.__keys:
                if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                    discarded_key = self.__keys.pop(0)
                    del self.cache_data[discarded_key]
            else:
                self.__keys.remove(key)
            self.__keys.append(key)
        return discarded_key
