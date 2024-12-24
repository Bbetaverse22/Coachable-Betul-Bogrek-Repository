"""1004. Max Consecutive Ones III"""

from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        Given a binary array nums and an integer k, 
        this function returns the maximum number of consecutive 1s in the array
        if you can flip at most k 0s.
        """
        left = 0
        max_length = 0
        zero_count = 0

        for right, value in enumerate(nums):
            if value == 0:
                zero_count += 1

            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
