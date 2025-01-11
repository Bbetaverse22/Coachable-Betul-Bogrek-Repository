"""173. Binary Search Tree Iterator"""

class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        """
        Initialize a TreeNode.
        
        Args:
            val (int): The value of the node.
            left (TreeNode, optional): The left child of the node. Defaults to None.
            right (TreeNode, optional): The right child of the node. Defaults to None.
        """
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    """Binary Search Tree Iterator that iterates over the nodes in ascending order."""
    def __init__(self, root: TreeNode):
        """
        Initialize the iterator with the root of the BST.
        
        Args:
            root (TreeNode): The root of the binary search tree.
        """
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        Return the next smallest number in the BST.
        
        Returns:
            int: The next smallest number.
        """
        topmost_node = self.stack.pop()
        node = topmost_node.right
        while node:
            self.stack.append(node)
            node = node.left
        return topmost_node.val

    def hasNext(self) -> bool:
        """
        Return whether the iterator has more nodes to iterate over.
        
        Returns:
            bool: True if there are more nodes, False otherwise.
        """
        return len(self.stack) > 0
