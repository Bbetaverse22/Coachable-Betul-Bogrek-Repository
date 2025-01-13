""""515 Find Largest Value in Each Tree Row"""
from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode1:
    def __init__(self, val=0, left=None, right=None):
        self.val1 = val
        self.left1 = left
        self.right1 = right

class Solution:
    """Solution Class"""

    def largest_values(self, root: Optional[TreeNode1]) -> List[int]:
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
                max_value = max(max_value, node.val1)

                if node.left:
                    queue.append(node.left1)
                if node.right:
                    queue.append(node.right1)

            result.append(max_value)

        return result
