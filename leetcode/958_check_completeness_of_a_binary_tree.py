"""958. Check Completeness of a Binary Tree"""
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """Solution Class"""

    def is_complete_tree(self, root: Optional[TreeNode]) -> bool:
        """
        This function checks if a binary tree is complete.
        """
        if not root:
            return True

        queue = deque([root])
        end = False

        while queue:
            node = queue.popleft()

            if not node:
                end = True
            else:
                if end:
                    return False
                queue.append(node.left)
                queue.append(node.right)

        return True
