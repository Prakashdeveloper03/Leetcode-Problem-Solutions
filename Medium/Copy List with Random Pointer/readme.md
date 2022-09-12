# Copy List with Random Pointer
![made-with-Python](https://img.shields.io/badge/Made%20with-Python-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a **deep copy** of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes `X` and `Y` in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, `x.random --> y`.

Return the head of the *copied linked list*.

__Example 1:__
```
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
```
__Example 2:__
```
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
```
__Example 3:__
```
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
```

__Constraints:__
- 0 <= n <= 1000
- -10<sup>4</sup> <= Node.val <= 10<sup>4</sup>
- Node.random is null or is pointing to some node in the linked list.

### Solution
```py
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
```