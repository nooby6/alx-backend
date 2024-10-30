#!/usr/bin/env python3
"""
LFU Cache module implementing a caching system based on
Least Frequently Used (LFU) with Least Recently Used (LRU) tie-breaking.
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache defines a caching system using the Least Frequently Used (LFU)
    replacement policy with a Least Recently Used (LRU) tie-breaking rule.
    """

    def __init__(self):
        """
        Initialize the LFUCache class.
        """
        super().__init__()
        self.usage_count = {}  # Dictionary to track usage frequency of keys
        self.lru_tracker = {}  # Dictionary to track order of access for LRU
        self.access_time = 0   # Counter to maintain access order for LRU

    def put(self, key, item):
        """
        Add an item to the cache using LFU eviction strategy.
        If the cache exceeds its maximum size, the least frequently used item
        will be discarded, with ties broken by the least recently used item.

        Args:
            key (str): The key to add to the cache.
            item (any): The value to associate with the key.
        """
        if key is None or item is None:
            return

        # If key exists, update its value, frequency, and access time
        if key in self.cache_data:
            self.cache_data[key] = item
            self.usage_count[key] += 1
            self.access_time += 1
            self.lru_tracker[key] = self.access_time
        else:
            # If cache is at capacity, apply LFU with LRU tie-breaking
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the LFU key(s), breaking ties with LRU
                min_freq = min(self.usage_count.values())
                lfu_keys = [k for k, v in self.usage_count.items() if v == min_freq]
                lru_key = min(lfu_keys, key=lambda k: self.lru_tracker[k])

                # Discard the LRU key among the least frequently used keys
                print(f"DISCARD: {lru_key}")
                del self.cache_data[lru_key]
                del self.usage_count[lru_key]
                del self.lru_tracker[lru_key]

            # Add the new item to cache
            self.cache_data[key] = item
            self.usage_count[key] = 1
            self.access_time += 1
            self.lru_tracker[key] = self.access_time

    def get(self, key):
        """
        Retrieve an item from the cache by key, if it exists.
        Updates the access frequency and access time for the key.

        Args:
            key (str): The key to retrieve from the cache.

        Returns:
            any: The value associated with the key, or None if the key is not found.
        """
        if key is None or key not in self.cache_data:
            return None
        # Update frequency and access time for the key
        self.usage_count[key] += 1
        self.access_time += 1
        self.lru_tracker[key] = self.access_time
        return self.cache_data[key]
