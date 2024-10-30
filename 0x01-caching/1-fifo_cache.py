#!/usr/bin/env python3
"""Contains a caching system implementation, with replacement."""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """A caching system with FIFO replacement"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Adds an item to the cache under the given key.
        FIFO algorithm used to discard items if cache is full.
        """
        if not key or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > self.MAX_ITEMS:
            first = list(self.cache_data)[0]
            del self.cache_data[first]
            print(f"DISCARD: {first}")

    def get(self, key):
        """Returns the cached item with the given key."""
        if not key:
            return None
        return self.cache_data.get(key)