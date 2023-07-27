#!/usr/bin/python3
'''
inherits from BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the first item put in cache (FIFO algorithm)
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.
'''

from base_caching import BaseCaching
from collections import OrderedDict as OD


class FIFOCache(BaseCaching):
    '''Allows storing and retrieving items using FIFO
    removal mechanism when the limit is reached.
    '''

    def __init__(self):
        'Initializes the cache.'
        super().__init__()
        self.cache_data = OD()

    def put(self, key, item):
        'Adds an item in the cache.'

        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        'Retrieves an item by key.'
        return self.cache_data.get(key, None)
