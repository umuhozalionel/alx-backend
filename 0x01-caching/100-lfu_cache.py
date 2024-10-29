#!/usr/bin/env python3
""" LFUCache module """

from base_caching import BaseCaching

class LFUCache(BaseCaching):
    """ LFUCache inherits from BaseCaching and implements a LFU caching system """

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.frequency = {}
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lfu_keys = [k for k, v in sorted(self.frequency.items(), key=lambda item: item[1])]
                lru_keys = [k for k in self.order if k in lfu_keys]
                discard_key = lru_keys[0]
                print(f"DISCARD: {discard_key}")
                del self.cache_data[discard_key]
                del self.frequency[discard_key]
                self.order.remove(discard_key)

            self.cache_data[key] = item
            self.frequency[key] = 1
            self.order.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        self.order.append(self.order.pop(self.order.index(key)))
        return self.cache_data[key]

