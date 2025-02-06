"""19. Remove Nth Node From End of List"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

class Solution:
    """Solution Class"""

    def remove_nth_from_end(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        This function removes the n-th node from the end of the list
        and returns the head of the modified list.
        """
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        slow = dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next
