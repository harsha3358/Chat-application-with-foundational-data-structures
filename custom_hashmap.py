class CustomHashMap:
    def __init__(self, size=10):
        self.size = size
        self.map = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash(key)
        bucket = self.map[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))

    def get(self, key):
        index = self._hash(key)
        bucket = self.map[index]

        for k, v in bucket:
            if k == key:
                return v
        return None

    def contains(self, key):
        return self.get(key) is not None