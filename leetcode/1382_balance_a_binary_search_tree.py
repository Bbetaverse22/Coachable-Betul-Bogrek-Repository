"""1382. Balance a Binary Search Tree"""

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """Solution Class"""

    def balanceBST(self, root: TreeNode) -> TreeNode:
        """
        This function balances a binary search tree.
        """
        def inorder_traversal(node: Optional[TreeNode]) -> List[int]:
            if not node:
                return []
            return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)

        def sorted_array_to_bst(nums: List[int]) -> Optional[TreeNode]:
            if not nums:
                return None
            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            root.left = sorted_array_to_bst(nums[:mid])
            root.right = sorted_array_to_bst(nums[mid+1:])
            return root

        sorted_values = inorder_traversal(root)
        return sorted_array_to_bst(sorted_values)
