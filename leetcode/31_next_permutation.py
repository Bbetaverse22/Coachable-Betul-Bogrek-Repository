"""31. Next Permutation"""
from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Rearranges numbers into the lexicographically next greater permutation of numbers.
        If such an arrangement is not possible, it must rearrange it as the lowest possible order.
        
        :param nums: List of integers to find the next permutation.
        """
        n = len(nums)
        i = n - 2

        # Step 1: Find the breakpoint
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # Step 2: Find the smallest element larger than nums[i]
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Swap nums[i] and nums[j]
            nums[i], nums[j] = nums[j], nums[i]

        # Step 3: Reverse the subarray to the right of i
        nums[i + 1:] = reversed(nums[i + 1:])