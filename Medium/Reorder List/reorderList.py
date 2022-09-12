from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev, curr = None, slow

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        while prev.next:
            tempa = head.next
            tempb = prev.next
            head.next = prev
            prev.next = tempa
            head = tempa
            prev = tempb
