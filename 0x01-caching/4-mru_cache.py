#!/usr/bin/env python3
""" MRUCache module """

from base_caching import BaseCaching

class MRUCache(BaseCaching):
    """ MRUCache inherits from BaseCaching and implements a MRU caching system """

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                most_recent = self.order.pop()
                print(f"DISCARD: {most_recent}")
                del self.cache_data[most_recent]
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data.get(key)
        return None
