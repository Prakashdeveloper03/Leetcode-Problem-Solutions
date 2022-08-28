# Valid Anagram
![made-with-Python](https://img.shields.io/badge/Made%20with-Python-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Given two strings `s` and `t`, return `true` if t is an anagram of s, and `false` otherwise.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

__Example 1:__
```
Input: s = "anagram", t = "nagaram"
Output: true
```
__Example 2:__
```
Input: s = "rat", t = "car"
Output: false
```

__Constraints:__
- 1 <= s.length, t.length <= 5 * 10<sup>4</sup>
- s and t consist of lowercase English letters.
  
### Solution
```py
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        t = input()
        print(Solution().isAnagram(s, t))
```