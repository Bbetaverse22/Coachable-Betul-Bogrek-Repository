"""528. Random Pick with Weight"""
import random
from typing import List

class Solution:
    """A class used to pick an index based on weights."""
    def __init__(self, w: List[int]):
        """Initializes the Solution with a list of weights."""
        self.prefix_sums = []
        cumulative_sum = 0
        for weight in w:
            cumulative_sum += weight
            self.prefix_sums.append(cumulative_sum)
        self.total_weight = cumulative_sum

    def pickIndex(self) -> int:
        """Picks an index based on the weights."""
        target = random.randint(1, self.total_weight)
        left, right = 0, len(self.prefix_sums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if self.prefix_sums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
