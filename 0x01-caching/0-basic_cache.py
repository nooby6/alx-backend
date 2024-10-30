#!/usr/bin/env python3
"""A caching system implementation."""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A caching system"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Adds an item to the cache"""
        if key is None or item is None:
            return

        self.cache_data[key] = item

    def get(self, key):
        """Returns the cached value linked to key"""
        if key is None:
            return None

        return self.cache_data.get(key)
