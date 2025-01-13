"""133. Clone Graph"""

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        """
        Clone an undirected graph. Each node in the graph contains a label
        and a list of its neighbors.
        """
        if not node:
            return node

        visited = {}

        def dfs(node):
            if node in visited:
                return visited[node]

            # Clone the node
            clone = Node(node.val, [])
            visited[node] = clone

            # Clone all the neighbors
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)
