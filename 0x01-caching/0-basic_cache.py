#!/usr/bin/env python3


"""
This module illustrates how to do simple caching
in python
"""

BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """
    A prety basic caching  system implementation
    """

    def __init__(self):
        """
        The constructor
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache
        Args:
            key (str): the key for the cache
            item (str): the value to se
        Returns:
            Returns None (explicitly)
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Let's get the cache item by the key
        Args:
            key (str): Key to the item
        Returns:
            if key in self.cached_items, return the
            item, None otherwise
        """
        return self.cache_data.get(key)
