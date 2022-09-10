# Find All Anagrams in a String
![made-with-Python](https://img.shields.io/badge/Made%20with-Python-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Given two strings `s` and `p`, return an array of all the start indices of `p`'s anagrams in `s`. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

__Example 1:__
```
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
```
__Example 2:__
```
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
```

__Constraints:__
- 1 <= s.length, p.length <= 3 * 10<sup>4</sup>
- s and p consist of lowercase English letters.

### Solution
```py
from collections import deque, Counter, defaultdict
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        stat_p = Counter(p)
        stat_s = defaultdict(int)
        ind, queue = 0, deque([])
        ans = []
        while ind != len(s):
            if s[ind] not in stat_p:
                while queue:
                    pop = queue.popleft()
                    stat_s[pop[0]] -= 1
            else:
                queue.append((s[ind], ind))
                stat_s[s[ind]] += 1
            if len(queue) == len(p):
                pop = queue.popleft()
                if not set(stat_p.items()) ^ set(stat_s.items()):
                    ans.append(pop[1])
                stat_s[pop[0]] -= 1
            ind += 1
        return ans

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s, p = input().strip().split()
        print(Solution().findAnagrams(s, p))
```