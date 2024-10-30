#!/usr/bin/env python3
"""
LRU Cache module implementing a caching system based on
Least Recently Used (LRU) eviction strategy.
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache defines a caching system using the Least Recently Used (LRU)
    replacement policy, where the least recently used item is discarded
    when the cache exceeds its maximum size.
    """

    def __init__(self):
        """
        Initialize the LRUCache class.
        """
        super().__init__()
        self.order = []  # List to track the order of usage for LRU

    def put(self, key, item):
        """
        Add an item to the cache using LRU eviction strategy.
        If the cache exceeds its maximum size, the least recently used item
        will be discarded.

        Args:
            key (str): The key to add to the cache.
            item (any): The value to associate with the key.
        """
        if key is None or item is None:
            return

        # Update the key if it already exists
        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Remove the least recently used item
            lru_key = self.order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

        # Add the item to the cache and update the order list
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """
        Retrieve an item from the cache by key, if it exists.
        Updates the least recently used key.

        Args:
            key (str): The key to retrieve from the cache.

        Returns:
            any: The value associated with the key, or None if the key is not found.
        """
        if key is None or key not in self.cache_data:
            return None

        # Update the order list to mark the key as recently used
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
