# Length of Last Word
![made-with-Python](https://img.shields.io/badge/Made%20with-Python-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Given a string s consisting of words and spaces, return the length of the **last word in the string**.

A word is a maximal substring consisting of non-space characters only.

__Example 1:__
```
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
```
__Example 2:__
```
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
```
__Example 3:__
```
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
```

__Constraints:__
- 1 <= s.length <= 10<sup>4</sup>
- `s` consists of only English letters and spaces ' '.
- There will be at least one word in `s`.


### Solution
```py
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split()[-1])

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = int(input())
        print(Solution().lengthOfLastWord(s))
```