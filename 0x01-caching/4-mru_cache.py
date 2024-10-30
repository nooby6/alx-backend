from base_caching import BaseCaching

class MRUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.order = []  # This will keep track of the order of keys for MRU

    def put(self, key, item):
        if key is None or item is None:
            return
        
        if key in self.cache_data:
            # Update the existing item and move the key to the end of the order list
            self.cache_data[key] = item
            self.order.remove(key)
            self.order.append(key)
        else:
            # If the cache is full, discard the most recently used item
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                mru_key = self.order.pop()  # Get the last key (most recently used)
                del self.cache_data[mru_key]  # Remove it from the cache
                print(f"DISCARD: {mru_key}")  # Print the discarded key
            
            # Add the new item to the cache
            self.cache_data[key] = item
            self.order.append(key)  # Add the new key to the order list

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        
        # Move the accessed key to the end of the order list to mark it as recently used
        self.order.remove(key)
        self.order.append(key)
        
        return self.cache_data[key]