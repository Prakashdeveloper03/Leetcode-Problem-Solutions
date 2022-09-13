# Add Two Numbers II
![made-with-Python](https://img.shields.io/badge/Made%20with-Python-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

You are given two **non-empty** linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

__Example 1:__
```
Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]
```
__Example 2:__
```
Input: l1 = [0], l2 = [0]
Output: [0]
```
__Example 3:__
```
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]
```

__Constraints:__
- The number of nodes in each linked list is in the range [1, 100].
- 0 <= Node.val <= 9
- It is guaranteed that the list represents a number that does not have leading zeros.

### Solution
```py
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        arr1 = ""
        arr2 = ""
        a1 = ListNode(0)
        a2 = a1
        while l1:
            arr1 += str(l1.val)
            l1 = l1.next
        while l2:
            arr2 += str(l2.val)
            l2 = l2.next
        ans = list(str(int(arr1) + int(arr2)))
        for an in ans:
            a2.next = ListNode(an)
            a2 = a2.next
        return a1.next
```