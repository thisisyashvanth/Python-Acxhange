# In case of Collision -> Linear Probing

class HashMap:
    def __init__(self, size):
        self.size = size
        self.buckets = [None] * size
    
    def hash(self, key):
        return hash(key) % self.size
    
    def put(self, key, value):
        index = self.hash(key)
        while self.buckets[index] is not None:
            k, _ = self.buckets[index]
            if k == key:
                self.buckets[index] = (key, value)
                return
            index = (index + 1) % self.size
        self.buckets[index] = (key, value)
    
    def get(self, key):
        index = self.hash(key)
        while self.buckets[index] is not None:
            k, v = self.buckets[index]
            if k == key:
                return v
            index = (index + 1) % self.size
        return None
    
    # Without Tombstone
    # [ _, _, age, name, city ] Remove name
    # [ _, _, age, _, city ]
    # when trying to get("city") with hash 3 supposedly
    # At index 3 you see None, so your loop stops
    # But city is at index 4
    def remove(self, key):
        index = self.hash(key)
        while self.buckets[index] is not None:
            k, v = self.buckets[index]
            if k == key:
                self.buckets[index] = None
                return True
            index = (index + 1) % self.size
        return False