"""498. Diagonal Traverse"""

from typing import List

class Solution:
    """A class used to find the diagonal order traversal of a matrix."""

    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        """
        Returns the diagonal order traversal of the given matrix.
        
        Args:
            mat (List[List[int]]): The input matrix.
        
        Returns:
            List[int]: The diagonal order traversal of the matrix.
        """
        if not mat or not mat[0]:
            return []

        rows, cols = len(mat), len(mat[0])
        result, intermediate = [], []

        for d in range(rows + cols - 1):
            intermediate.clear()
            r = 0 if d < cols else d - cols + 1
            c = d if d < cols else cols - 1

            while r < rows and c > -1:
                intermediate.append(mat[r][c])
                r += 1
                c -= 1

            if d % 2 == 0:
                result.extend(intermediate[::-1])
            else:
                result.extend(intermediate)

        return result
