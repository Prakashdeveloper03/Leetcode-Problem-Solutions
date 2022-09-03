# Add Binary
![made-with-Python](https://img.shields.io/badge/Made%20with-Python-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Given two binary strings `a` and `b`, return their sum as a binary string.

__Example 1:__
```
Input: a = "11", b = "1"
Output: "100"
```
__Example 2:__
```
Input: a = "1010", b = "1011"
Output: "10101"
```

__Constraints:__
- 1 <= a.length, b.length <= 10<sup>4</sup>
- a and b consist only of '0' or '1' characters.
- Each string does not contain leading zeros except for the zero itself.


### Solution
```py
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a, b = input().split()
        print(Solution().addBinary(a, b))
```