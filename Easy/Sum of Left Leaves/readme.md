# Sum of Left Leaves
![made-with-Python](https://img.shields.io/badge/Made%20with-Python-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Given the `root` of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A **left leaf** is a leaf that is the left child of another node.

__Example 1:__
```
Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
```
__Example 2:__
```
Input: root = [1]
Output: 0
```

__Constraints:__
- The number of nodes in the tree is in the range [1, 1000].
- -1000 <= Node.val <= 1000
  
### Solution
```py
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
```