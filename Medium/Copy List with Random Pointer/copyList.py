from typing import Optional


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = x
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        oldCopyDict = {None: None}
        curr = head
        while curr:
            copy = Node(curr.val)
            oldCopyDict[curr] = copy
            curr = curr.next
        curr = head

        while curr:
            copy = oldCopyDict[curr]
            copy.next = oldCopyDict[curr.next]
            copy.random = oldCopyDict[curr.random]
            curr = curr.next
        return oldCopyDict[head]
