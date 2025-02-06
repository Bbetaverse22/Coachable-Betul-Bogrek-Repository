"""380. Insert Delete GetRandom O(1)"""

import random

class RandomizedSet:
    """RandomizedSet Class"""

    def __init__(self):
        """Initializes the data structure."""
        self.map = {}
        self.array = []

    def insert(self, val: int) -> bool:
        """Inserts a value to the set. Returns true if the set did not
        already contain the specified element."""
        if val in self.map:
            return False
        self.map[val] = len(self.array)
        self.array.append(val)
        return True

    def remove(self, val: int) -> bool:
        """Removes a value from the set. Returns true if the set contained
        the specified element."""
        if val not in self.map:
            return False
        last_element = self.array[-1]
        idx = self.map[val]
        self.array[idx] = last_element
        self.map[last_element] = idx
        self.array.pop()
        del self.map[val]
        return True

    def get_random(self) -> int:
        """Get a random element from the set."""
        return random.choice(self.array)
