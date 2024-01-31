#!/usr/bin/env python3

from threading import RLock
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """lfu class"""
    def __init__(self):
        """initialize"""
        super().__init__()
        self.__stats, self.__rlock = {}, RLock()

    def put(self, key, item):
        """put in cache"""
        if key and item:
            with self.__rlock:
                Outer = self._balance(key)
                self.cache_data[key] = item
                if Outer:
                    print(f'DISCARD: {Outer}')

    def get(self, key):
        """get item"""
        with self.__rlock:
            value = self.cache_data.get(key)
            if value:
                self.__stats[key] += 1
        return value

    def _balance(self, keyIn):
        """balance"""
        with self.__rlock:
            Outer = None
            bs = BaseCaching.MAX_ITEMS
            if len(self.cache_data) == bs and keyIn not in self.__stats:
                Outer = min(self.__stats, key=self.__stats.get)
                self.cache_data.pop(Outer)
                self.__stats.pop(Outer)
            self.__stats[keyIn] = self.__stats.get(keyIn, 0) + 1
        return Outer
