"""958. Check Completeness of a Binary Tree"""
from collections import deque

class Solution:
    """Solution Class"""

    def is_complete_tree(self, root) -> bool:
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
