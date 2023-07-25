![img](https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png)


![We got some cash don't we?](https://media3.giphy.com/media/xT8qBfxbxaS8DRPnUY/200w.webp?cid=ecf05e47n04xlbi6x3srxxf5c42uidr5mjgbc1e5luvrtdse&ep=v1_gifs_search&rid=200w.webp&ct=g)

## About
Caching is a computing technique that involves temporarily storing frequently accessed data or computations in a cache, which is a high-speed memory located closer to the processor. This setup enables faster access to data compared to retrieving it from the main memory or disk storage.

Caching is done primarily  to enhance system performance and minimize latency. By holding commonly used data or computations in the cache, subsequent requests for the same data can be fulfilled more swiftly, eliminating the need to repeat resource-intensive or time-consuming processes. As a result, users experience quicker response times, improved interactions, and reduced strain on the underlying data storage infrastructure.

## Resources
__Read or watch__:

1. [Cache replacement policies - FIFO]()
2. [Cache replacement policies - LIFO]()
3. [Cache replacement policies - LRU]()
4. [Cache replacement policies - MRU]()
5. [Cache replacement policies - LFU]()


## Learning objectives
By the end of this project, you are expected to be able to [explain to anyone]() __Without the help of Google__:

- [X] What a caching system is
- [X] What FIFO means
- [X] What LIFO means
- [X] What LRU means
- [X] What MRU means
- [X] What LFU means
- [X] What the purpose of a caching system
- [X] What limits a caching system have


## More Info
## Parent class `BaseCaching`

All your classes must inherit from `BaseCaching` defined below:

```python
#!/usr/bin/python3
""" BaseCaching module
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
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")
```