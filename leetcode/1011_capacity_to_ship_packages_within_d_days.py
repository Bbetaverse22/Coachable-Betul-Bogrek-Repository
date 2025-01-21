"""1011. Capacity To Ship Packages Within D Days"""

from typing import List

class Solution:
    """Solution Class"""

    def shipWithinDays(self, weights: List[int], D: int) -> int:
        """
        This function finds the least weight capacity of a ship
        that will result in all the packages being shipped within D days.
        """
        def canShip(capacity: int) -> bool:
            days = 1
            current_weight = 0
            for weight in weights:
                if current_weight + weight > capacity:
                    days += 1
                    current_weight = 0
                current_weight += weight
                if days > D:
                    return False
            return True

        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            if canShip(mid):
                right = mid
            else:
                left = mid + 1
        return left
