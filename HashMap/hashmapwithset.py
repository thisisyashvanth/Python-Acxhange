class HashMap:
    def __init__(self, size):
        self.size = size
        self.buckets = [set() for _ in range(size)]
    
    def hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self.hash(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                bucket.remove((k, v))
                break
        bucket.add((key, value))

    def get(self, key):
        index = self.hash(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        return None
    
    def remove(self, key):
        index = self.hash(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                bucket.remove((k, v))
                return True
        return False