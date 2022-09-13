from typing import Optional


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        def rec(l1, l2, tmp=0):
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            if l1 or l2 or tmp > 0:
                if l1_val + l2_val + tmp >= 10:
                    l1.val = (l1_val + l2_val + tmp) % 10
                    tmp = 1
                    if not l1.next:
                        l1.next = ListNode(0)
                else:
                    l1.val = l2_val + l1_val + tmp
                    tmp = 0
                    if l2 and l2.next and not l1.next:
                        l1.next = ListNode(0)
            else:
                return
            rec(l1.next, l2.next if l2 else None, tmp)

        rec(l1, l2)
        return l1
