"""1424. Diagonal Traverse II"""

from typing import List
from collections import defaultdict

class Solution:
    """Solution Class"""

    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        """
        This function returns the diagonal order traversal of a 2D list.
        """
        diagonals = defaultdict(list)
        for i, row in enumerate(nums):
            for j, value in enumerate(row):
                diagonals[i + j].append(value)

        result = []
        for k in sorted(diagonals.keys()):
            result.extend(reversed(diagonals[k]))

        return result
