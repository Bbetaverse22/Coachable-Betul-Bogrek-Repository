"""236 Lowest Common Ancestor of a Binary Tree"""
class TreeNode:
    def __init__(self, val_1=0, left_1=None, right_1=None):
        self.val = val_1
        self.left = left_1
        self.right = right_1

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """Find the lowest common ancestor of two nodes in a binary tree."""
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left if left else right
