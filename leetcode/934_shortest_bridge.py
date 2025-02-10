"""Shortest Bridge Solution"""
from collections import deque
from typing import List

class Solution:

    def shortest_bridge(self, grid: List[List[int]]) -> int:
        """
        Finds the shortest distance to connect two islands in the grid.
        """
        n = len(grid)
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = [[False]*n for _ in range(n)]

        def dfs(x, y, queue):
            stack = [(x, y)]
            visited[x][y] = True
            while stack:
                i, j = stack.pop()
                queue.append((i, j, 0))
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == 1:
                        visited[nx][ny] = True
                        stack.append((nx, ny))

        # Find first island
        queue = deque()
        found = False
        for i in range(n):
            if found: break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j, queue)
                    found = True
                    break

        # BFS from the boundary of first island to find second island
        while queue:
            x, y, dist = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    if grid[nx][ny] == 1:
                        return dist
                    queue.append((nx, ny, dist + 1))
                    visited[nx][ny] = True
        return -1
