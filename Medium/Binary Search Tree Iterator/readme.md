# Binary Search Tree Iterator
![made-with-Python](https://img.shields.io/badge/Made%20with-Python-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):
- **BSTIterator(TreeNode root)** Initializes an object of the `BSTIterator` class. The `root` of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
- **boolean hasNext()** Returns `true` if there exists a number in the traversal to the right of the pointer, otherwise returns `false`.
- **int next()** Moves the pointer to the right, then returns the number at the pointer.

Notice that by initializing the pointer to a non-existent smallest number, the first call to *next()* will return the smallest element in the BST.

You may assume that `next()` calls will always be valid. That is, there will be at least a next number in the in-order traversal when `next()` is called.

__Example:__
```
Input
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
Output
[null, 3, 7, true, 9, true, 15, true, 20, false]

Explanation
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    // return 3
bSTIterator.next();    // return 7
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 9
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 15
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 20
bSTIterator.hasNext(); // return False
```

__Constraints:__
- The number of nodes in the tree is in the range [1, 10<sup>5</sup>].
- 0 <= Node.val <= 10<sup>6</sup>
- At most 10<sup>5</sup> calls will be made to hasNext, and next.


### Solution
```py
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
```