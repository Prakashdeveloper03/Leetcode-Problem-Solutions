# Rotate List
![made-with-Python](https://img.shields.io/badge/Made%20with-Python-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Given the `head` of a linked list, rotate the list to the right by `k` places.

__Example 1:__
```
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
```
__Example 2:__
```
Input: head = [0,1,2], k = 4
Output: [2,0,1]
```

__Constraints:__
- The number of nodes in the list is in the range [0, 500].
- -100 <= Node.val <= 100
- 0 <= k <= 2 * 10<sup>9</sup>


### Solution
```py
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        temp = head
        length = 1

        while temp.next:
            temp = temp.next
            length += 1

        temp.next = head
        k %= length
        n = length - k

        while n:
            temp = temp.next
            n -= 1

        head = temp.next
        temp.next = None
        return head
```