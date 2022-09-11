# Smallest Range II
![made-with-Python](https://img.shields.io/badge/Made%20with-Python-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

You are given an integer array `nums` and an integer `k`.

For each index i where `0 <= i < nums.length`, change `nums[i]` to be either `nums[i] + k` or `nums[i] - k`.

The score of nums is the difference between the maximum and minimum elements in nums.

Return the minimum **score of nums** after changing the values at each index.

__Example 1:__
```
Input: nums = [1], k = 0
Output: 0
Explanation: The score is max(nums) - min(nums) = 1 - 1 = 0.
```
__Example 2:__
```
Input: nums = [0,10], k = 2
Output: 6
Explanation: Change nums to be [2, 8]. The score is max(nums) - min(nums) = 8 - 2 = 6.
```
__Example 3:__
```
Input: nums = [1,3,6], k = 3
Output: 3
Explanation: Change nums to be [4, 6, 3]. The score is max(nums) - min(nums) = 6 - 3 = 3.
```

__Constraints:__
- 1 <= nums.length <= 10<sup>4</sup>
- 0 <= nums[i] <= 10<sup>4</sup>
- 0 <= k <= 10<sup>4</sup>

### Solution
```py
from typing import List

class Solution:
    def smallestRangeII(self, lis: List[int], k: int) -> int:
        lis.sort()
        ans = lis[-1] - lis[0]
        for i in range(1, len(lis)):
            l = lis[:i]
            r = lis[i:]
            mini = min(l[0] + k, r[0] - k)
            maxi = max(l[-1] + k, r[-1] - k)
            ans = min(ans, maxi - mini)
        return ans

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        lis = list(map(int, input().strip().split()))
        k = int(input())
        print(Solution().smallestRangeII(lis, k))
```