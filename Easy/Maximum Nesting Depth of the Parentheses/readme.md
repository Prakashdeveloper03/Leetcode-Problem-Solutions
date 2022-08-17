# Maximum Nesting Depth of the Parentheses
![made-with-Python](https://img.shields.io/badge/Made%20with-Python-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

A string is a valid parentheses string (denoted **VPS**) if it meets one of the following:
- It is an empty string "", or a single character not equal to "(" or ")",
- It can be written as AB (A concatenated with B), where A and B are **VPS**'s, or
- It can be written as (A), where A is a **VPS**.

We can similarly define the nesting depth depth(S) of any **VPS** S as follows:
- depth("") = 0
- depth(C) = 0, where C is a string with a single character not equal to "(" or ")".
- depth(A + B) = max(depth(A), depth(B)), where A and B are **VPS**'s.
- depth("(" + A + ")") = 1 + depth(A), where A is a **VPS**.

For example, "", "()()", and "()(()())" are **VPS**'s (with nesting depths 0, 1, and 2), and ")(" and "(()" are not **VPS**'s.

Given a **VPS** represented as string s, return the nesting depth of s.

__Example 1:__
```
Input: s = "(1+(2*3)+((8)/4))+1"
Output: 3
Explanation: Digit 8 is inside of 3 nested parentheses in the string.
```
__Example 2:__
```
Input: s = "(1)+((2))+(((3)))"
Output: 3
```

__Constraints:__
- 1 <= s.length <= 100
- `s` consists of digits 0-9 and characters '+', '-', '*', '/', '(', and ')'.
- It is guaranteed that parentheses expression `s` is a VPS.


### Solution
```py
from operator import add
from itertools import accumulate

class Solution:
    def maxDepth(self, s: str) -> int:
        s = "".join((filter(lambda x: x in ["(", ")"], s)))
        if not s:
            return 0
        chars = [1 if ch == "(" else -1 for ch in s]
        return max(accumulate(chars, add))

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        print(Solution().maxDepth(s))
```