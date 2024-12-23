"""636 Exclusive Time of Functions"""
from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        """
        Given the number of functions and a list of logs, 
        this function returns the exclusive time of each function.
        """
        result = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            func_id, typ, time = log.split(':')
            func_id, time = int(func_id), int(time)

            if typ == 'start':
                if stack:
                    result[stack[-1]] += time - prev_time
                stack.append(func_id)
                prev_time = time
            else:
                result[stack.pop()] += time - prev_time + 1
                prev_time = time + 1

        return result
