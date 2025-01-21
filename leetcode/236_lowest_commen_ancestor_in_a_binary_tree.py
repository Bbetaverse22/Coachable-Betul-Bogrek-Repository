"""236 Lowest Common Ancestor of a Binary Tree"""
class TreeNode3:
    def __init__(self, val3=0, left3=None, right3=None):
        self.val3 = val3
        self.left3 = left3
        self.right3 = right3

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode3', p: 'TreeNode3', q: 'TreeNode3') -> 'TreeNode3':
        """Find the lowest common ancestor of two nodes in a binary tree."""
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left if left else right
