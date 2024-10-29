#!/usr/bin/env python3
""" LIFOCache module """

from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """ LIFOCache inherits from BaseCaching and implements a LIFO caching system """

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_key = self.last_key
                if last_key is not None:
                    print(f"DISCARD: {last_key}")
                    del self.cache_data[last_key]
            self.cache_data[key] = item
            self.last_key = key

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
