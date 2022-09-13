# Add Two Numbers
![made-with-Python](https://img.shields.io/badge/Made%20with-Python-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

You are given two **non-empty linked lists** representing two non-negative integers. The digits are stored in *reverse order*, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number `0` itself.

__Example 1:__
```
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
```
__Example 2:__
```
Input: l1 = [0], l2 = [0]
Output: [0]
```
__Example 3:__
```
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
```

__Constraints:__
- The number of nodes in each linked list is in the range [1, 100].
- 0 <= Node.val <= 9
- It is guaranteed that the list represents a number that does not have leading zeros.

### Solution
```py
from typing import Optional

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        def rec(l1, l2, tmp=0):
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            if l1 or l2 or tmp > 0:
                if l1_val + l2_val + tmp >= 10:
                    l1.val = (l1_val + l2_val + tmp) % 10
                    tmp = 1
                    if not l1.next:
                        l1.next = ListNode(0)
                else:
                    l1.val = l2_val + l1_val + tmp
                    tmp = 0
                    if l2 and l2.next and not l1.next:
                        l1.next = ListNode(0)
            else:
                return
            rec(l1.next, l2.next if l2 else None, tmp)

        rec(l1, l2)
        return l1
```