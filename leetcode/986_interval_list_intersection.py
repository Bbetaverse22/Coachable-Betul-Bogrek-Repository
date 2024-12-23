"""986. Interval List Intersections"""

from typing import List

class Solution:
    """A class used to find the intersections of two interval lists."""

    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        """
        Returns the intersection of two interval lists.
        
        Args:
            firstList (List[List[int]]): The first list of intervals.
            secondList (List[List[int]]): The second list of intervals.
        
        Returns:
            List[List[int]]: The list of intersecting intervals.
        """
        i, j = 0, 0
        result = []

        while i < len(firstList) and j < len(secondList):
            lo = max(firstList[i][0], secondList[j][0])
            hi = min(firstList[i][1], secondList[j][1])

            if lo <= hi:
                result.append([lo, hi])

            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return result
