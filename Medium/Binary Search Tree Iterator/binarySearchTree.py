from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.deq = []
        self.traverse(root)

    def next(self) -> int:
        if self.deq:
            return self.deq.pop(0)

    def hasNext(self) -> bool:
        return bool(self.deq)

    def traverse(self, node):
        if node:
            self.traverse(node.left)
            self.deq.append(node.val)
            self.traverse(node.right)
