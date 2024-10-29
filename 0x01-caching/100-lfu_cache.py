#!/usr/bin/env python3
""" LFUCache module """

from base_caching import BaseCaching

class LFUCache(BaseCaching):
    """ LFUCache inherits from BaseCaching and implements a LFU caching system """

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.frequency = {}
        self.usage_order = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.frequency[key] += 1
            else:
                self.frequency[key] = 1

            if key in self.cache_data:
                self.usage_order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                least_freq = min(self.frequency.values())
                least_freq_keys = [k for k, v in self.frequency.items() if v == least_freq]
                if len(least_freq_keys) > 1:
                    oldest = sorted([(self.usage_order.index(k), k) for k in least_freq_keys])[0][1]
                else:
                    oldest = least_freq_keys[0]
                print(f"DISCARD: {oldest}")
                del self.cache_data[oldest]
                del self.frequency[oldest]
                self.usage_order.remove(oldest)

            self.cache_data[key] = item
            self.usage_order.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            self.frequency[key] += 1
            self.usage_order.remove(key)
            self.usage_order.append(key)
            return self.cache_data[key]
        return None
