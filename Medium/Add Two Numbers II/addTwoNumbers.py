from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        arr1 = ""
        arr2 = ""
        a1 = ListNode(0)
        a2 = a1
        while l1:
            arr1 += str(l1.val)
            l1 = l1.next
        while l2:
            arr2 += str(l2.val)
            l2 = l2.next
        ans = list(str(int(arr1) + int(arr2)))
        for an in ans:
            a2.next = ListNode(an)
            a2 = a2.next
        return a1.next
