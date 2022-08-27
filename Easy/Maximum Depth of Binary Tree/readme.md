# Maximum Depth of Binary Tree
![made-with-Python](https://img.shields.io/badge/Made%20with-Python-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Given the `root` of a binary tree, return its maximum depth.

A binary tree's **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node.

__Example 1:__
```
Input: root = [3,9,20,null,null,15,7]
Output: 3
```
__Example 2:__
```
Input: root = [1,null,2]
Output: 2
```

__Constraints:__
- The number of nodes in the tree is in the range [0, 10<sup>4</sup>].
- -100 <= Node.val <= 100

  
### Solution
```py
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return (
            1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root else 0
        )
```