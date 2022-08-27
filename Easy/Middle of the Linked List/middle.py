from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        while temp and temp.next:
            head = head.next
            temp = temp.next.next
        return head
