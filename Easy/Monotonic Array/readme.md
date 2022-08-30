# Monotonic Array
![made-with-Python](https://img.shields.io/badge/Made%20with-Python-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

An array is **monotonic** if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all `i <= j`, `nums[i] <= nums[j]`. An array `nums` is monotone decreasing if for all `i <= j`, `nums[i] >= nums[j]`.

Given an integer array nums, return `true` if the given array is monotonic, or `false` otherwise.

__Example 1:__
```
Input: nums = [1,2,2,3]
Output: true
```
__Example 2:__
```
Input: nums = [6,5,4,4]
Output: true
```

__Example 3:__
```
Input: nums = [1,3,2]
Output: false
```

__Constraints:__
- 1 <= nums.length <= 10<sup>5</sup>
- -10<sup>5</sup> <= nums[i] <= 10<sup>5</sup>


### Solution
```py
from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        return nums in [sorted(nums), sorted(nums, reverse=True)]

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        nums = list(map(int, input().strip().split()))
        print(Solution().isMonotonic(nums))
```