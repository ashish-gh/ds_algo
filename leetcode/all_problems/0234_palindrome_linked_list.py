from operator import le
from typing import Optional


class ListNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


class Solution:
    def is_palindrome(self, head: Optional[ListNode]):
        # Solution 1: Iterative method with numbers
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        l, r = 0, len(nums)
        while l < r:
            if nums[l] != nums[r]:
                return False
            l += 1
            r -= 1
        return True

    def is_palindrome_1(self, head: Optional[ListNode]):
        # Solution 2: Two pointer method in Linked list
        slow, fast = head, head
        # find the middle : slow pointer
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse the second hald
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        # prev determines the last pointer and slow reaches the end of the linked lsit

        # check similarity
        left, right = head, prev
        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
