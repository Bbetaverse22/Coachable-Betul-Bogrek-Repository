"""207. Course Schedule"""
from typing import List

class Solution:
    """Solution Class"""

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        This function determines if it is possible to finish all courses given the prerequisites.
        """
        graph = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            graph[course].append(pre)

        visited = [0] * numCourses

        def dfs(node):
            if visited[node] == -1:
                return False
            if visited[node] == 1:
                return True
            visited[node] = -1
            for pre in graph[node]:
                if not dfs(pre):
                    return False
            visited[node] = 1
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
