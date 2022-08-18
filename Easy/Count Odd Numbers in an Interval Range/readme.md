# Count Odd Numbers in an Interval Range
![made-with-Python](https://img.shields.io/badge/Made%20with-Python-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Given two non-negative integers `low` and `high`. Return the count of odd numbers between low and high (inclusive).

__Example 1:__
```
Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].
```
__Example 2:__
```
Input: low = 8, high = 10
Output: 1
Explanation: The odd numbers between 8 and 10 are [9].
```

__Constraints:__
- 0 <= low <= high <= 10^9

### Solution
```py
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (0 if not low % 2 and not high % 2 else 1) + (high - low) // 2

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        low = int(input())
        high = int(input())
        print(Solution().countOdds(low, high))
```