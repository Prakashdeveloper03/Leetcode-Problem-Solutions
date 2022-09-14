from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        temp = head
        length = 1

        while temp.next:
            temp = temp.next
            length += 1

        temp.next = head
        k %= length
        n = length - k

        while n:
            temp = temp.next
            n -= 1

        head = temp.next
        temp.next = None
        return head
