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
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                diagonals[i + j].append(nums[i][j])

        result = []
        for k in sorted(diagonals.keys()):
            result.extend(reversed(diagonals[k]))

        return result
