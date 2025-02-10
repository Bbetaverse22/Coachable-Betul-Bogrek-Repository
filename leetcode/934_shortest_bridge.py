"""Shortest Bridge Solution"""
from collections import deque
from typing import List

class Solution:

    def shortest_bridge(self, grid: List[List[int]]) -> int:
        """
        Finds the shortest distance to connect two islands in the grid.
        """
        n = len(grid)
        visited = [[False]*n for _ in range(n)]

        def dfs(x, y, queue):
            stack = [(x, y)]
            visited[x][y] = True
            while stack:
                i, j = stack.pop()
                queue.append((i, j, 0))
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == 1:
                        visited[nx][ny] = True
                        stack.append((nx, ny))

        def find_first_island():
            queue = deque()
            for i in range(n):
                for j in range(n):
                    if grid[i][j] == 1:
                        dfs(i, j, queue)
                        return queue
            return None

        queue = find_first_island()
        while queue:
            x, y, dist = queue.popleft()
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    if grid[nx][ny] == 1:
                        return dist
                    queue.append((nx, ny, dist + 1))
                    visited[nx][ny] = True
        return -1
