import random
from typing import List

class Solution:
    """
    Solution class for the problem of picking a random index for a given target.
    """

    def __init__(self, nums: List[int]):
        """
        Initializes the object with the list of numbers.
        """
        self.nums = nums

    def pick(self, target: int) -> int:
        """
        Picks a random index for the given target number.
        """
        while True:
            index = random.randint(0, len(self.nums) - 1)
            if target == self.nums[index]:
                return index

