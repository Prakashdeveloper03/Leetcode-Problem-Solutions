from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def checkNextNode(self, head, root):
        checkLeft, checkRight = False, False
        if not head:
            return True
        if root.left and root.left.val == head.val:
            checkLeft = self.checkNextNode(head.next, root.left)
        if root.right and root.right.val == head.val:
            checkRight = self.checkNextNode(head.next, root.right)

        return checkLeft or checkRight

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if root.val == head.val and self.checkNextNode(head.next, root):
            return True
        checkLeft = self.isSubPath(head, root.left)
        checkRight = self.isSubPath(head, root.right)
        return checkLeft or checkRight
