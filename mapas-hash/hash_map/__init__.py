class Node:
    def __init__(self, label, value):
        self.label = label
        self.value = value

    def __str__(self):
        value_repr = f"\"{self.value}\"" if type(self.value) == str else self.value
        return f"'{self.label}': {value_repr}"

class Map:
    def __init__(self):
        self.number_of_buckets = 5
        self.buckets = [[] for _ in range(self.number_of_buckets)]
        self.length = 0
        self.expand_threshold = 0.75
        self.reduce_threshold = 0.2
        self.resize_factor = 2

    def __len__(self):
        return self.length

    @property
    def ocupation(self):
        return self.length / self.number_of_buckets

    def _resize(self, new_size):
        old_buckets = self.buckets
        self.number_of_buckets = new_size
        self.buckets = [[] for _ in range(self.number_of_buckets)]
        self.length = 0
        for bucket in old_buckets:
            for node in bucket:
                self[node.label] = node.value
        return

    def __setitem__(self, key, value):
        key = str(key)
        hashed_key = hash(key)
        bucket_index = hashed_key % self.number_of_buckets
        bucket = self.buckets[bucket_index]
        for node in bucket:
            if node.label == key:
                node.value = value
                return
        bucket.append(Node(key, value))
        self.length += 1
        if self.ocupation > self.expand_threshold:
            self._resize(self.number_of_buckets * self.resize_factor)

    def __getitem__(self, key):
        key = str(key)
        hashed_key = hash(key)
        bucket_index = hashed_key % self.number_of_buckets
        bucket = self.buckets[bucket_index]
        for node in bucket:
            if node.label == key:
                return node.value

    def __delitem__(self, key):
        key = str(key)
        hashed_key = hash(key)
        bucket_index = hashed_key % self.number_of_buckets
        bucket = self.buckets[bucket_index]
        i = 0
        for node in bucket:
            if node.label == key:
               del bucket[i] 
               self.length -= 1
               if self.ocupation < self.reduce_threshold:
                   self._resize(int(self.number_of_buckets / self.resize_factor))
               return
            i += 1

    def __iter__(self):
        for bucket in self.buckets:
            for node in bucket:
                yield node.label, node.value

    def __str__(self):
        repr = "{"
        i = 0
        for bucket in self.buckets:
            for node in bucket:
                 i += 1
                 if i != len(self):
                     repr += f"{node}, "
                 else:
                     repr += f"{node}"
        repr += "}"
        return repr
