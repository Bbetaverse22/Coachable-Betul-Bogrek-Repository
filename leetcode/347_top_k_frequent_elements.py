"""347. Top K Frequent Elements"""

import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Returns the k most frequent elements in the given list.
        
        Args:
            nums (List[int]): The list of integers.
            k (int): The number of top frequent elements to return.
        
        Returns:
            List[int]: The list of k most frequent elements.
        """
        # Step 1: Count the frequency of each element
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1

        # Step 2: Use a min-heap to keep track of the top k frequent elements
        min_heap = []
        for num, freq in freq_map.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # Step 3: Extract the elements from the heap
        return [num for freq, num in min_heap]
