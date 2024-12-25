""""515 Find Largest Value in Each Tree Row"""
from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """Solution Class"""

    def largest_values(self, root: Optional[TreeNode]) -> List[int]:
        """
        This function finds the largest value in each row of a binary tree.
        """

        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            max_value = float('-inf')

            for _ in range(level_size):
                node = queue.popleft()
                max_value = max(max_value, node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(max_value)

        return result
