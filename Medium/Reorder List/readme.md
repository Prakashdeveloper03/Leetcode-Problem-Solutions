# Reorder List
![made-with-Python](https://img.shields.io/badge/Made%20with-Python-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

You are given the head of a singly linked-list. The list can be represented as:
```
L0 → L1 → … → Ln - 1 → Ln
```
Reorder the list to be on the following form:
```
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
```
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

__Example 1:__
```
Input: head = [1,2,3,4]
Output: [1,4,2,3]
```
__Example 2:__
```
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
```

__Constraints:__
- The number of nodes in the list is in the range [1, 5 * 10<sup>4</sup>].
- 1 <= Node.val <= 1000

### Solution
```py
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev, curr = None, slow

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        while prev.next:
            tempa = head.next
            tempb = prev.next
            head.next = prev
            prev.next = tempa
            head = tempa
            prev = tempb
```