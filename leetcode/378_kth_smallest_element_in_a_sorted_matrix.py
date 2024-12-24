"""378 Kth Smallest Element in a Sorted Matrix"""
from typing import List
import heapq

class Solution:
    """Solution Class"""

    def kth_smallest(self, matrix: List[List[int]], k: int) -> int:
        """
        This function finds the k-th smallest element in a sorted matrix.
        """

        min_heap = []

        for row in matrix:
            for element in row:
                heapq.heappush(min_heap, element)

        for _ in range(k - 1):
            heapq.heappop(min_heap)

        return heapq.heappop(min_heap)
