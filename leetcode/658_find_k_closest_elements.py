"""658 Find K Closest Elements"""
from typing import List

class Solution:
    """Solution Class"""

    def find_closest_elements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        This function finds the k closest elements to x in the array.
        """
        left, right = 0, len(arr) - k

        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left:left + k]
