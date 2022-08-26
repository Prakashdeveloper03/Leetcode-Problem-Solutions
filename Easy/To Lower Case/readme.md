# To Lower Case
![made-with-Python](https://img.shields.io/badge/Made%20with-Python-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Given a string `s`, return the string after replacing every uppercase letter with the same lowercase letter.

__Example 1:__
```
Input: s = "Hello"
Output: "hello"
```
__Example 2:__
```
Input: s = "here"
Output: "here"
```
__Example 3:__
```
Input: s = "LOVELY"
Output: "lovely"
```

__Constraints:__
- 1 <= s.length <= 100
- s consists of printable ASCII characters.
  
### Solution
```py
class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        print(Solution().toLowerCase(s))
```