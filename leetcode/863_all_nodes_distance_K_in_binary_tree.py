"""863 All Nodes Distance K in Binary Tree"""
from collections import defaultdict, deque
from typing import List

class TreeNode:
    """
    Definition for a binary tree node.
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        """
        Finds all nodes at distance K from the target node in the binary tree.
        """
        def build_graph(node, parent):
            if node:
                if parent:
                    graph[node.val].append(parent.val)
                    graph[parent.val].append(node.val)
                build_graph(node.left, node)
                build_graph(node.right, node)

        graph = defaultdict(list)
        build_graph(root, None)

        queue = deque([(target.val, 0)])
        seen = {target.val}
        result = []

        while queue:
            node, dist = queue.popleft()
            if dist == K:
                result.append(node)
            elif dist < K:
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        queue.append((neighbor, dist + 1))

        return result
