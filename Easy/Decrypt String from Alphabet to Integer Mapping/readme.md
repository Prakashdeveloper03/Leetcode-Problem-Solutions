# Decrypt String from Alphabet to Integer Mapping
![made-with-Python](https://img.shields.io/badge/Made%20with-Python-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

You are given a string s formed by digits and '#'. We want to map s to English lowercase characters as follows:

- Characters ('a' to 'i') are represented by ('1' to '9') respectively.
- Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.

Return the string formed after mapping.

The test cases are generated so that a unique mapping will always exist.

__Example 1:__
```
Input: s = "10#11#12"
Output: "jkab"
Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
```
__Example 2:__
```
Input: s = "1326#"
Output: "acz"
```

__Constraints:__
- 1 <= s.length <= 1000
- s consists of digits and the '#' letter.
- s will be a valid string such that mapping is always possible.

  
### Solution
```py
import string

class Solution:
    def freqAlphabets(self, s: str) -> str:
        result = []
        i = 0
        alphabets = string.ascii_lowercase
        while i < len(s):
            if (i + 1 < len(s) and s[i + 1] == "#") or s[i] == "#":
                i += 1
                continue
            elif i + 2 < len(s) and s[i + 2] == "#":
                result.append(alphabets[int(s[i : i + 2]) - 1])
            else:
                result.append(alphabets[int(s[i]) - 1])
            i += 1
        return "".join(result)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        print(Solution().freqAlphabets(s))
```