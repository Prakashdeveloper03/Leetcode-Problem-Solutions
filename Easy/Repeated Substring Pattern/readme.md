# Repeated Substring Pattern
![made-with-Python](https://img.shields.io/badge/Made%20with-Python-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Given a string `s`, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

__Example 1:__
```
Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.
```
__Example 2:__
```
Input: s = "aba"
Output: false
```
__Example 3:__
```
Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
```

__Constraints:__
- 1 <= s.length <= 10<sup>4</sup>
- `s` consists of lowercase English letters.

### Solution
```py
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in s[1:] + s[:-1]

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        print(Solution().repeatedSubstringPattern(s))
```