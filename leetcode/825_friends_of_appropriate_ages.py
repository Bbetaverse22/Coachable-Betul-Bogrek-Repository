"""825. Friends Of Appropriate Ages"""
from typing import List

class Solution:
    """Solution Class"""

    def num_friend_requests(self, ages: List[int]) -> int:
        """
        This function counts the number of friend requests made based on age constraints.
        """
        ages.sort()
        
        freq = [0] * 121
        for age in ages:
            freq[age] += 1
        
        total_requests = 0
        
        for age_a in range(1, 121):
            if freq[age_a] == 0:
                continue
            for age_b in range(1, 121):
                if freq[age_b] == 0:
                    continue
                if age_b <= 0.5 * age_a + 7:
                    continue
                if age_b > age_a:
                    continue
                if age_b > 100 and age_a < 100:
                    continue
                total_requests += freq[age_a] * (freq[age_b] - (age_a == age_b))
        
        return total_requests
