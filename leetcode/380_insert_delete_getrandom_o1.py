"""380. Insert Delete GetRandom O(1)"""
import random

class RandomizedSet:
    """RandomizedSet Class"""

    def __init__(self):
        self.hashMap = {}
        self.valuesList = []
        
    def insert(self, val: int) -> bool:
        if val in self.hashMap:
            return False
        self.valuesList.append(val)
        self.hashMap[val] = len(self.valuesList) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hashMap:
            return False
        idx = self.hashMap[val]
        last = self.valuesList[-1]
        self.valuesList[idx] = last
        self.hashMap[last] = idx
        self.valuesList.pop()
        del self.hashMap[val]
        return True
        
    def getRandom(self) -> int:
        return random.choice(self.valuesList)
