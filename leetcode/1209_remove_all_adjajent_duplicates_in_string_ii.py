"""1209. Remove All Adjacent Duplicates in String II"""
from typing import List

class Solution:
    """Solution Class"""

    def remove_duplicates(self, s: str, k: int) -> str:
        """
        This function removes all adjacent duplicates in a string where a duplicate is defined as a substring of length k.
        """
        stack = []

        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([char, 1])

        result = ''.join(char * count for char, count in stack)
        return result
