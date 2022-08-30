# Implement strStr()
![made-with-Python](https://img.shields.io/badge/Made%20with-Python-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Implement `strStr()`.

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

**Clarification:**

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return `0` when needle is an **empty string**. This is consistent to C's `strstr()` and Java's `indexOf()`.

__Example 1:__
```
Input: haystack = "hello", needle = "ll"
Output: 2
```
__Example 2:__
```
Input: haystack = "aaaaa", needle = "bba"
Output: -1
```

__Constraints:__
- 1 <= haystack.length, needle.length <= 10<sup>4</sup>
- haystack and needle consist of only lowercase English characters.


### Solution
```py
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        haystack, needle = input().strip().split()
        print(Solution().strStr(haystack, needle))
```