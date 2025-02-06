"""621. Task Scheduler"""

import heapq
from typing import List

class Solution:
    """Solution Class"""

    def least_interval(self, tasks: List[str], n: int) -> int:
        """
        This function calculates the least number of units of times
        that the CPU will take to finish all the given tasks.
        """

        task_counts = {}
        for task in tasks:
            if task in task_counts:
                task_counts[task] += 1
            else:
                task_counts[task] = 1

        max_heap = [-count for count in task_counts.values()]
        heapq.heapify(max_heap)

        time = 0
        while max_heap:
            temp = []
            for _ in range(n + 1):
                if max_heap:
                    temp.append(heapq.heappop(max_heap))

            for count in temp:
                if count + 1 < 0:
                    heapq.heappush(max_heap, count + 1)

            time += n + 1 if max_heap else len(temp)

        return time
