"""200. Number of Islands"""
from typing import List

class Solution:
    """A class used to solve the Number of Islands problem."""

    def numIslands(self, grid: List[List[str]]) -> int:
        """Counts the number of islands in the given grid.
        Args:
            grid (List[List[str]]): A 2D grid map of '1's (land) and '0's (water).
        Returns:
            int: The number of islands.
        """
        if not grid:
            return 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == '0':
                return
            grid[r][c] = '0'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        num_islands = 0
        for r, row in enumerate(grid):
            for c, value in enumerate(row):
                if value == '1':
                    dfs(r, c)
                    num_islands += 1

        return num_islands
