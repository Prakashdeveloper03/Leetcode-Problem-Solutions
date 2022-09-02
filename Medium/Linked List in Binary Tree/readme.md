# Linked List in Binary Tree
![made-with-Python](https://img.shields.io/badge/Made%20with-Python-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Given a binary tree `root` and a linked list with head as the first node.

Return True if all the elements in the linked list starting from the `head` correspond to some *downward path* connected in the binary tree otherwise return False.

In this context downward path means a path that starts at some node and goes downwards.

__Example 1:__
```
Input: head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true
Explanation: Nodes in blue form a subpath in the binary Tree.
```
__Example 2:__
```
Input: head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true
```
__Example 3:__
```
Input: head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: false
Explanation: There is no path in the binary tree that contains all the elements of the linked list from head.
```

__Constraints:__
- The number of nodes in the tree will be in the range [1, 2500].
- The number of nodes in the list will be in the range [1, 100].
- 1 <= Node.val <= 100 for each node in the linked list and binary tree.

### Solution
```py
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
```