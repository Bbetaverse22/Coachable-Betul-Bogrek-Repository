"""Spiral Matrix"""
from typing import List

class Solution:

    def spiral_order(self, matrix: List[List[int]]) -> List[int]:
        """
        Returns the elements of the matrix in spiral order.
        """
        result = []
        if not matrix:
            return result

        top, bottom, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1

        while left <= right and top <= bottom:
            for c in range(left, right + 1):
                result.append(matrix[top][c])
            top += 1

            for r in range(top, bottom + 1):
                result.append(matrix[r][right])
            right -= 1

            if top <= bottom:
                for c in range(right, left - 1, -1):
                    result.append(matrix[bottom][c])
                bottom -= 1

            if left <= right:
                for r in range(bottom, top - 1, -1):
                    result.append(matrix[r][left])
                left += 1

        return result
