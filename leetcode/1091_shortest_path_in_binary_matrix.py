"""1091. Shortest Path in Binary Matrix"""
from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """Find the shortest path in a binary matrix."""
        N = len(grid)
        q = deque([(0,0,1)]) # r, c, length
        visited = set((0,0))
        directions = [[0,1], [1,0], [0,-1], [-1,0], [1,1], [1,-1], [-1,1], [-1,-1]]

        while q:
            r,c,length = q.popleft()
            if min(r,c) < 0 or max(r,c) >= N or grid[r][c] == 1:
                continue
            if r == N-1 and c == N-1:
                return length
            for dr, dc in directions:
                if (r+dr, c+dc) not in visited:
                    q.append((r+dr, c+dc, length+1))
                    visited.add((r+dr, c+dc))
        return -1
