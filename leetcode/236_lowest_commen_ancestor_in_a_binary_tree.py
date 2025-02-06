"""236 Lowest Common Ancestor of a Binary Tree"""

class TreeNode4:
    def __init__(self, val4=0, left4=None, right4=None):
        self.val = val4
        self.left = left4
        self.right = right4

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode4',
    p: 'TreeNode4', q: 'TreeNode4') -> 'TreeNode4':
        """Find the lowest common ancestor of two nodes in a binary tree."""
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left if left else right
