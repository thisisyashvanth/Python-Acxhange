class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]
    
    def hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self.hash(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
    
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
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False

hm = HashMap()
hm.put("name", "Yash")
hm.put("age", 22)
