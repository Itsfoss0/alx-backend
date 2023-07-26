#!/usr/bin/env python3


"""
This module illustrates how to do simple caching
in python
"""


class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("Not implemented")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("Not implemeted")


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
