"""865. Smallest Subtree with all the Deepest Nodes"""

from typing import Tuple

# Definition for a binary tree node.
class TreeNode2:
    def __init__(self, val2=0, left2=None, right2=None):
        self.val2 = val2
        self.left2 = left2
        self.right2 = right2

class Solution:
    """Solution Class"""

    def subtreeWithAllDeepest(self, root: TreeNode2) -> TreeNode2:
        """
        This function finds the smallest subtree containing all the deepest nodes.
        """        
        def dfs(node: TreeNode2) -> Tuple[int, TreeNode2]:
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
