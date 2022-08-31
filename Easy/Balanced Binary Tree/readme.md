# Balanced Binary Tree
![made-with-Python](https://img.shields.io/badge/Made%20with-Python-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.


__Example 1:__
```
Input: root = [3,9,20,null,null,15,7]
Output: true
```
__Example 2:__
```
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
```
__Example 3:__
```
Input: root = []
Output: true
```

__Constraints:__
- The number of nodes in the tree is in the range [0, 5000].
- -10<sup>4</sup> <= Node.val <= 10<sup>4</sup>

### Solution
```py
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    balanced = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        self.height(root)
        return self.balanced

    def height(self, root):
        if root is None:
            return 0
        l = self.height(root.left)
        r = self.height(root.right)
        if abs(l - r) > 1:
            self.balanced = False
        return max(l, r) + 1
```