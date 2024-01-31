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
            Outer = self._balance(key)
            with self.__rlock:
                self.cache_data.update({key: item})
            if Outer is not None:
                print('DISCARD: {}'.format(Outer))

    def get(self, key):
        """Get an item"""
        with self.__rlock:
            value = self.cache_data.get(key, None)
            if key in self.__stats:
                self.__stats[key] += 1
        return value

    def _balance(self, keyIn):
        """Removes the earliest item from the cache"""
        Outer = None
        with self.__rlock:
            if keyIn not in self.__stats:
                if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                    Outer = min(self.__stats, key=self.__stats.get)
                    self.cache_data.pop(Outer)
                    self.__stats.pop(Outer)
            self.__stats[keyIn] = self.__stats.get(keyIn, 0) + 1
        return Outer
