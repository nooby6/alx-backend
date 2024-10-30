#!/usr/bin/env python3
"""
MRU Cache module implementing a caching system based on
Most Recently Used (MRU) eviction strategy.
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache defines a caching system using the Most Recently Used (MRU)
    replacement policy, where the most recently used item is discarded
    when the cache exceeds its maximum size.
    """

    def __init__(self):
        """
        Initialize the MRUCache class.
        """
        super().__init__()
        self.recently_used = None  # Track the most recently used key

    def put(self, key, item):
        """
        Add an item to the cache using MRU eviction strategy.
        If the cache exceeds its maximum size, the most recently used item
        will be discarded.

        Args:
            key (str): The key to add to the cache.
            item (any): The value to associate with the key.
        """
        if key is None or item is None:
            return

        # If cache is at capacity and key is new, discard the MRU key
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
            if self.recently_used is not None:
                print(f"DISCARD: {self.recently_used}")
                del self.cache_data[self.recently_used]

        # Add or update the cache with the new item
        self.cache_data[key] = item
        self.recently_used = key  # Update the MRU key

    def get(self, key):
        """
        Retrieve an item from the cache by key, if it exists.
        Updates the most recently used key.

        Args:
            key (str): The key to retrieve from the cache.

        Returns:
            any: The value associated with the key, or None if the key is not found.
        """
        if key is None or key not in self.cache_data:
            return None
        # Update the MRU key
        self.recently_used = key
        return self.cache_data[key]
