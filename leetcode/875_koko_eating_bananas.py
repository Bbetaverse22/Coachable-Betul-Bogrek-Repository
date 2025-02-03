from typing import List

class Solution:
    """Solution Class"""

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        This function calculates the minimum integer k such that
        Koko can eat all the bananas within h hours.
        """
        def canFinish(piles, k, h):
            hours = 0
            for pile in piles:
                hours += (pile + k - 1) // k
            return hours <= h

        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            if canFinish(piles, mid, h):
                right = mid
            else:
                left = mid + 1

        return left
