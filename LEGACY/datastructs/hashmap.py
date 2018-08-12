"""

A hashmap is just a set of (key, value) pairs. Key typically is an int or string. Each key must be unique.
One big advantage is search, insert, delete in O(1). Also called maps, dictionaries, hash tables or associate arrays.

For example:
KEYS      VALUES
Beans --> 1.85
Corn --> 2.38
Rice --> 1.92

Three main components:
    * Array = data structure used to store the data
    * Hash function = gets the hash of the value (math function left to choice)
        Example of a hash function = len(string) + 6
    * Another function to convert hash into an array index.
        NOTE: The hash function can just convert the original key into an array index, for a simpler hashmap.
        Example of NOTE: index = sum(ASCII_VALUE for each letter in key) % len(array)
    * Collision handling:
        - Collisions are when multiple (key, value) pairs match to the same cell in the array.
        - You can solve it by making each cell a datastructure, like a list, a linked list, etc.
        - You can also use other techniques like Linear Probing.

The performance of the hashmap depends on keeping the least amount of values in each cell of the array.
Because if you have a linked list of 5 elems in cell 3, it's going to take iterating through all of them potentially
to find the one you want, instead of just returning the value (if it was a linked list of 1 elem).

"""


class HashMap(object):
    def __init__(self, size):
        self.size = size
        self.map = [None] * self.size

    def _get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value_pair = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = key_value_pair
            return True
        else:
            # Collision detected
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value_pair)
            return True

    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True

    def show(self):
        for item in self.map:
            if item is not None:
                print(str(item))

h = HashMap(size=6)
h.add('Bob', '123-45678')
h.add('Ming', '290-8765')
h.add('Ming', '908-7652')
h.add('Alicia', '732-9876')
h.show()
h.delete('Bob')
h.show()