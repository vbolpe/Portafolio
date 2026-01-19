class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, string):
        total = 0
        for char in string:
            total += ord(char)
        return total

    def add(self, key, value):
        hash_key = self.hash(key)

        if hash_key not in self.collection:
            self.collection[hash_key] = {}

        self.collection[hash_key][key] = value

    def remove(self, key):
        hash_key = self.hash(key)

        if hash_key in self.collection:
            if key in self.collection[hash_key]:
                del self.collection[hash_key][key]

                if not self.collection[hash_key]:
                    del self.collection[hash_key]

    def lookup(self, key):
        hash_key = self.hash(key)

        if hash_key in self.collection:
            return self.collection[hash_key].get(key)

        return None
