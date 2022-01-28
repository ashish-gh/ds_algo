from typing import Optional


class ListNode:
    def __init__(self, val: int = 0) -> None:
        self.val = val
        self.next = None


class LinkedList:
    def reverse_linked_list(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Method 1
        # Iterative method with two pointers technique
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        prev, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev

        # Method 2
        # Recursive method
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        # if not head:
        #     return None

        # new_head = head
        # while head.next:
        #     new_head = self.reverse_linked_list(head)
        #     head.next.next = head
        # head.next = None
        # return new_head

