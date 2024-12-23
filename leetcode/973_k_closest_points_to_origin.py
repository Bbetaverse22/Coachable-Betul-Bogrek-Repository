"""973. K Closest Points to Origin"""
import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """ This function returns the k closest points to the origin. """
        result = []
        minHeap = []
        for x, y in points:
            distance = x * x + y * y
            minHeap.append([distance, x, y])
        heapq.heapify(minHeap)
        while k > 0:
            distance, x, y = heapq.heappop(minHeap)
            result.append([x, y])
            k -= 1

        return result
