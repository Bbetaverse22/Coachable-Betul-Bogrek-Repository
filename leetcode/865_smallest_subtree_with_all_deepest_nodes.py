"""865. Smallest Subtree with all the Deepest Nodes"""

from typing import Optional, Tuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """Solution Class"""

    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        """
        This function finds the smallest subtree containing all the deepest nodes.
        """        
        def dfs(node: TreeNode) -> Tuple[int, TreeNode]:
            if not node:
                return 0, None
            left_depth, left_subtree = dfs(node.left)
            right_depth, right_subtree = dfs(node.right)

            if left_depth > right_depth:
                return left_depth + 1, left_subtree
            elif right_depth > left_depth:
                return right_depth + 1, right_subtree
            else:
                return left_depth + 1, node

        return dfs(root)[1]
