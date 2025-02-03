from typing import List
from collections import defaultdict, deque

class Solution:
    """Solution Class"""

    def find_order(self, num_courses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        This function finds the order in which courses should be taken to finish all courses.
        """
        graph = defaultdict(list)
        in_degree = [0] * num_courses

        for dest, src in prerequisites:
            graph[src].append(dest)
            in_degree[dest] += 1

        queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
        order = []

        while queue:
            course = queue.popleft()
            order.append(course)

            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return order if len(order) == num_courses else []
