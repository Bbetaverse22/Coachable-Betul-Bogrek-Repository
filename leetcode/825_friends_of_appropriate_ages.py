"""825. Friends Of Appropriate Ages"""
from typing import List

class Solution:
    """Solution Class"""

    def num_friend_requests(self, ages: List[int]) -> int:
        """
        This function counts the number of friend requests made based on age constraints.
        """
        freq = [0] * 121
        for age in ages:
            freq[age] += 1

        total_requests = 0

        for age_a in range(1, 121):
            if freq[age_a] == 0:
                continue
            left = age_a // 2 + 8
            right = age_a + 1
            for age_b in range(left, right):
                if freq[age_b] == 0:
                    continue
                total_requests += freq[age_a] * (freq[age_b] - (age_a == age_b))

        return total_requests
