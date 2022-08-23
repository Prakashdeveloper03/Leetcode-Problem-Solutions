# Sum of All Odd Length Subarrays
![made-with-Python](https://img.shields.io/badge/Made%20with-Python-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Given an array of positive integers arr, return the **sum of all possible odd-length subarrays** of `arr`.

A subarray is a contiguous subsequence of the array.

__Example 1:__
```
Input: arr = [1,4,2,5,3]
Output: 58
Explanation: The odd-length subarrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
```
__Example 2:__
```
Input: arr = [1,2]
Output: 3
Explanation: There are only 2 subarrays of odd length, [1] and [2]. Their sum is 3.
```
__Example 3:__
```
Input: arr = [10,11,12]
Output: 66
```

__Constraints:__
- 1 <= arr.length <= 100
- 1 <= arr[i] <= 1000

### Solution
```py
from typing import List

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        lengths = [i + 1 for i in range(len(arr)) if i % 2 == 0]
        res = 0
        for l in lengths:
            for i in range(len(arr) + 1 - l):
                res += sum(arr[i : i + l])
        return res

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        print(Solution().sumOddLengthSubarrays(arr))
```