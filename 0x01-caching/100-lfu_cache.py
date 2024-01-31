#!/usr/bin/python3

"""
LFU Cache Class
"""

from threading import RLock


BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """LFU cache"""

    def __init__(self):
        """Instantiation method"""
        super().__init__()
        self.__stats = {}
        self.__rlock = RLock()

    def put(self, key, item):
        """Add item in the cache"""
        if key is not None and item is not None:
            with self.__rlock:
                Outer = self._balance(key)
                self.cache_data.update({key: item})
                if Outer is not None:
                    print('DISCARD: {}'.format(Outer))

    def get(self, key):
        """Get an item"""
        with self.__rlock:
            value = self.cache_data.get(key)
            if value is not None:
                self.__stats[key] += 1
        return value

    def _balance(self, keyIn):
        """Removes the earliest item from the cache"""
        with self.__rlock:
            Outer = None
            bs = BaseCaching.MAX_ITEMS
            if len(self.cache_data) == bs and keyIn not in self.__stats:
                Outer = min(self.__stats, key=self.__stats.get)
                self.cache_data.pop(Outer)
                self.__stats.pop(Outer)
            self.__stats[keyIn] = self.__stats.get(keyIn, 0) + 1
        return Outer
