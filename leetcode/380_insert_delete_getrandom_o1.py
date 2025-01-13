"""380. Insert Delete GetRandom O(1)"""

import random

class RandomizedSet:
    """RandomizedSet Class"""

    def __init__(self):
        """Initializes the data structure."""
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        """Inserts a value to the set. Returns true if the set did not
        already contain the specified element."""
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        """Removes a value from the set. Returns true if the set contained
        the specified element."""
        if val not in self.dict:
            return False
        last_element = self.list[-1]
        idx = self.dict[val]
        self.list[idx] = last_element
        self.dict[last_element] = idx
        self.list.pop()
        del self.dict[val]
        return True

    def get_random(self) -> int:
        """Get a random element from the set."""
        return random.choice(self.list)
