"""1382. Balance a Binary Search Tree"""

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode4:
    def __init__(self, val4=0, left4=None, right4=None):
        self.val4 = val4
        self.left4 = left4
        self.right4 = right4

class Solution:
    """Solution Class"""

    def balanceBST(self, root: TreeNode4) -> TreeNode4:
        """
        This function balances a binary search tree.
        """
        def inorder_traversal(node: Optional[TreeNode4]) -> List[int]:
            if not node:
                return []
            return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)

        def sorted_array_to_bst(nums: List[int]) -> Optional[TreeNode4]:
            if not nums:
                return None
            mid = len(nums) // 2
            root = TreeNode4(nums[mid])
            root.left = sorted_array_to_bst(nums[:mid])
            root.right = sorted_array_to_bst(nums[mid+1:])
            return root

        sorted_values = inorder_traversal(root)
        return sorted_array_to_bst(sorted_values)
