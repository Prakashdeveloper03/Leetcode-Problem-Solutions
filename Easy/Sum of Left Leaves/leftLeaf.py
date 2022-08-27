from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def traverse(root, isLeft):
            if root is None:
                return 0
            if root.left is None and root.right is None and isLeft:
                return root.val
            return traverse(root.left, True) + traverse(root.right, False)

        return traverse(root, False)
