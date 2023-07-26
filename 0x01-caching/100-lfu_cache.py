#!/usr/bin/env python3


"""
This module illustrates how to do simple caching
in python. This time, we will do FIFO caching.
If the cache is at maximum capacity, we will discard
the first item in and add the new one (FIFO)
"""

from collections import OrderedDict
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """
    A prety basic caching  system implementation
    Based on a FIFO list
    """

    def __init__(self):
        """
        The constructor
        """
        super().__init__()
        self.cache_data = OrderedDict(self.cache_data)

    def put(self, key, item):
        """
        Add an item to the cache
        Args:
            key (str): the key for the cache
            item (str): the value to se
        Returns:
            Returns None (explicitly)
        """

        if len(self.cache_data.keys()) >= super().MAX_ITEMS:
            last_key = list(self.cache_data.keys())[0]
            self.cache_data.pop(last_key)
            print(f'DISCARD: {last_key}')
        if key and item:
            self.cache_data[key] = item
            # self.cache_data.move_to_end(key, last=False)

    def get(self, key):
        """
        Let's get the cache item by the key
        Args:
            key (str): Key to the item
        Returns:
            if key in self.cached_items, return the
            item, None otherwise
        """
        if key in self.cache_data.keys():
            self.cache_data.move_to_end(key, last=True)
        return self.cache_data.get(key)
