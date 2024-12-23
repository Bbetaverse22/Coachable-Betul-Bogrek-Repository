"""146. LRU Cache"""

class Node:
    """A node in the doubly linked list."""
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.left = None
        self.right = None

class LRUCache:
    """A Least Recently Used (LRU) cache implemented with a doubly linked list and a hash map."""
    def __init__(self, capacity: int):
        """
        Initialize the LRU cache with a given capacity.
        
        :param capacity: The maximum number of items that can be stored in the cache.
        """
        self.capacity = capacity
        self.cache = {}

        # Dummy head and tail nodes to simplify insertion and removal
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.right = self.tail
        self.tail.left = self.head

    def insert(self, node: Node) -> None:
        """
        Insert a node right before the tail node.
        
        :param node: The node to be inserted.
        """
        previousNode = self.tail.left
        nextNode = self.tail
        previousNode.right = nextNode.left = node
        node.right = nextNode
        node.left = previousNode

    def remove(self, node: Node) -> None:
        """
        Remove a node from the doubly linked list.
        
        :param node: The node to be removed.
        """
        previousNode = node.left
        nextNode = node.right
        previousNode.right = nextNode
        nextNode.left = previousNode

    def get(self, key: int) -> int:
        """
        Get the value of the key if the key exists in the cache, otherwise return -1.
        
        :param key: The key to be retrieved.
        :return: The value associated with the key, or -1 if the key does not exist.
        """
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        """
        Update the value of the key if the key exists.
        Otherwise, add the key-value pair to the cache.
        If the cache exceeds its capacity, remove the least recently used item.
    
        :param key: The key to be added or updated.
        :param value: The value to be associated with the key.
        """
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.head.right
            self.remove(lru)
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key, value)
