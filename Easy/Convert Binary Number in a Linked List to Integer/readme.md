# Convert Binary Number in a Linked List to Integer
![made-with-Python](https://img.shields.io/badge/Made%20with-Python-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Given `head` which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

The **most significant bit** is at the head of the linked list.

__Example 1:__
```
Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10
```
__Example 2:__
```
Input: head = [0]
Output: 0
```

__Constraints:__
- The Linked List is not empty.
- Number of nodes will not exceed 30.
- Each node's value is either 0 or 1.
  
### Solution
```py
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        result = ""
        while head:
            result += str(head.val)
            head = head.next
        return int(result, 2)
```