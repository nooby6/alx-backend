#!/usr/bin/env python3
"""Contains a caching system implementation, with replacement."""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """A caching system with LIFO replacement"""

    def __init__(self):
        super().__init__()
        self._last_accessed = None

    def put(self, key, item):
        """Adds an item to the cache under the given key.
        LIFO algorithm used to discard items if cache is full.
        """
        if not key or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > self.MAX_ITEMS:
            del self.cache_data[self._last_accessed]
            print(f"DISCARD: {self._last_accessed}")

        self._last_accessed = key

    def get(self, key):
        """Returns the cached item with the given key."""
        if not key:
            return None
        return self.cache_data.get(key)