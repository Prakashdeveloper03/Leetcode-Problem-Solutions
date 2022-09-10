# Subarray Product Less Than K
![made-with-Python](https://img.shields.io/badge/Made%20with-Python-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Given an array of integers `nums` and an integer `k`, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than `k`.

__Example 1:__
```
Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
```
__Example 2:__
```
Input: nums = [1,2,3], k = 0
Output: 0
```

__Constraints:__
- 1 <= nums.length <= 3 * 10<sup>4</sup>
- 1 <= nums[i] <= 1000
- 0 <= k <= 10<sup>6</sup>

### Solution
```py
from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i, j = 0, 0
        mult = 1
        res = 0
        while mult < k and i < len(nums):
            mult *= nums[i]
            i += 1
            while mult >= k:
                mult /= nums[j]
                j += 1
            res += i - j
        return res

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        nums = list(map(int, input().strip().split()))
        k = int(input())
        print(Solution().numSubarrayProductLessThanK(nums, k))
```