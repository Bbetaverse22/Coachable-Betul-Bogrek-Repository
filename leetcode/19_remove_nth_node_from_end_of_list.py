"""19. Remove Nth Node From End of List"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """Solution Class"""

    def remove_nth_from_end(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        This function removes the nth node from the end of the list and returns the head of the modified list.
        """
        dummy = ListNode(0, head)
        first = dummy
        second = dummy

        for _ in range(n + 1):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next

        return dummy.next

