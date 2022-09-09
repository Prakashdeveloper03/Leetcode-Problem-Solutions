# Group Anagrams
![made-with-Python](https://img.shields.io/badge/Made%20with-Python-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

__Example 1:__
```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```
__Example 2:__
```
Input: strs = [""]
Output: [[""]]
```
__Example 3:__
```
Input: strs = ["a"]
Output: [["a"]]
```

__Constraints:__
- 1 <= strs.length <= 10<sup>4</sup>
- 0 <= strs[i].length <= 100
- `strs[i]` consists of lowercase English letters.


### Solution
```py
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for element in strs:
            if "".join(sorted(element)) not in group:
                group["".join(sorted(element))] = [element]
            else:
                group["".join(sorted(element))].extend([element])
        return list(group.values())

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        strs = list(input().strip().split())
        print(Solution().groupAnagrams(strs))
```