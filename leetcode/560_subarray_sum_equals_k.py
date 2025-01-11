"""560 Subarray Sum Equals K"""
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """Find the total number of continuous subarrays whose sum equals k."""
        total_count = 0
        freq_map = {0: 1}
        current_sum = 0

        for num in nums:
            current_sum += num
            if current_sum - k in freq_map:
                total_count += freq_map[current_sum - k]
            freq_map[current_sum] = freq_map.get(current_sum, 0) + 1

        return total_count
