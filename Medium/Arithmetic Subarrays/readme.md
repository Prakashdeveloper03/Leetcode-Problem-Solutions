# Arithmetic Subarrays
![made-with-Python](https://img.shields.io/badge/Made%20with-Python-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

A sequence of numbers is called arithmetic if it consists of at least two elements, and the difference between every two consecutive elements is the same. More formally, a sequence s is arithmetic if and only if `s[i+1] - s[i] == s[1] - s[0]` for all valid i.

For example, these are arithmetic sequences:
```
1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
```
The following sequence is not arithmetic:
```
1, 1, 2, 5, 7
```
You are given an array of `n` integers, nums, and two arrays of m integers each, l and r, representing the m range queries, where the ith query is the range `[l[i], r[i]]`. All the arrays are 0-indexed.

Return a list of boolean elements answer, where `answer[i]` is true if the subarray `nums[l[i]]`, `nums[l[i]+1]`, ... , `nums[r[i]]` can be rearranged to form an arithmetic sequence, and false otherwise.

__Example 1:__
```
Input: nums = [4,6,5,9,3,7], l = [0,0,2], r = [2,3,5]
Output: [true,false,true]
Explanation:
In the 0th query, the subarray is [4,6,5]. This can be rearranged as [6,5,4], which is an arithmetic sequence.
In the 1st query, the subarray is [4,6,5,9]. This cannot be rearranged as an arithmetic sequence.
In the 2nd query, the subarray is [5,9,3,7]. This can be rearranged as [3,5,7,9], which is an arithmetic sequence.
```
__Example 2:__
```
Input: nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], l = [0,1,6,4,8,7], r = [4,4,9,7,9,10]
Output: [false,true,false,false,true,true]
```

__Constraints:__
- n == nums.length
- m == l.length
- m == r.length
- 2 <= n <= 500
- 1 <= m <= 500
- 0 <= l[i] < r[i] < n
- -10<sup>5</sup> <= nums[i] <= 10<sup>5</sup>

### Solution
```py
from typing import List


class Solution:
    def checkArithmeticSubarrays(
        self, nums: List[int], l: List[int], r: List[int]
    ) -> List[bool]:
        ans = [True] * len(l)
        for i in range(len(l)):
            test = sorted(nums[l[i] : r[i] + 1])
            dif = test[1] - test[0]
            for j in range(len(test) - 1):
                if test[j + 1] - test[j] != dif:
                    ans[i] = False
                    break
        return ans


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        nums = list(map(int, input().split()))
        l = list(map(int, input().split()))
        r = list(map(int, input().split()))
        print(Solution().checkArithmeticSubarrays(nums, l, r))
```