"""695. Max Area of Island"""
from typing import List

class Solution:
    """Solution Class"""

    def max_area_of_island(self, grid: List[List[int]]) -> int:
        """
        This function finds the maximum area of an island in a given 2D grid.
        """
        if not grid or not grid[0]:
            return 0

        max_area = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return 0

            grid[i][j] = 0  # Mark the cell as visited
            area = 1  # Current cell

            for di, dj in directions:
                area += dfs(i + di, j + dj)

            return area

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))

        return max_area
