"""523 Continuous Subarray Sum"""
from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """Check if the array has a subarray whose sum is a multiple of k."""
        if k == 0:
            return any(nums[i] == 0 and nums[i + 1] == 0 for i in range(len(nums) - 1))

        prefix_sum = 0
        mod_map = {0: -1}

        for i, num in enumerate(nums):
            prefix_sum += num
            mod = prefix_sum % k
            if mod in mod_map:
                if i - mod_map[mod] > 1:
                    return True
            else:
                mod_map[mod] = i

        return False
