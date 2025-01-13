"""378 Kth Smallest Element in a Sorted Matrix"""
from typing import List
import heapq

class Solution:
    """Solution Class"""

    def kth_smallest(self, matrix: List[List[int]], k: int) -> int:
        """
        This function finds the k-th smallest element in a sorted matrix.
        """

        n = len(matrix)
        min_heap = [(matrix[i][0], i, 0) for i in range(n)]
        heapq.heapify(min_heap)

        for _ in range(k - 1):
            _, row, column = heapq.heappop(min_heap)
            if column + 1 < n:
                heapq.heappush(min_heap, (matrix[row][column + 1], row, column + 1))

        return heapq.heappop(min_heap)[0]
