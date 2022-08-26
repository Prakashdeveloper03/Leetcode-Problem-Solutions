# Verifying an Alien Dictionary
![made-with-Python](https://img.shields.io/badge/Made%20with-Python-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different `order`. The `order` of the alphabet is some permutation of lowercase letters.

Given a sequence of `words` written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

__Example 1:__
```
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
```
__Example 2:__
```
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
```
__Example 3:__
```
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character
```

__Constraints:__
- 1 <= words.length <= 100
- 1 <= words[i].length <= 20
- order.length == 26
- All characters in words[i] and order are English lowercase letters.
  
### Solution
```py
from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_index = {key: index for index, key in enumerate(order)}
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            for j in range(len(word1)):
                if j == len(word2):
                    return False
                if word1[j] != word2[j]:
                    if order_index.get(word2[j]) < order_index.get(word1[j]):
                        return False
                    break
        return True

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        words = list(input().split())
        order = input()
        print(Solution().isAlienSorted(words, order))
```