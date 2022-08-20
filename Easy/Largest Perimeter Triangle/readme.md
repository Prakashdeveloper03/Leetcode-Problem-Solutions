# Largest Perimeter Triangle
![made-with-Python](https://img.shields.io/badge/Made%20with-Python-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Given an integer array `nums`, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return `0`.

__Example 1:__
```
Input: nums = [2,1,2]
Output: 5
```
__Example 2:__
```
Input: nums = [1,2,1]
Output: 0
```

__Constraints:__
- 3 <= nums.length <= 10<sup>4</sup>
- 1 <= nums[i] <= 10<sup>6</sup>

### Solution
```py
from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        return next(
            (
                sum(nums[idx - 3 : idx])
                for idx in range(3, len(nums) + 1)
                if nums[idx - 3] < nums[idx - 2] + nums[idx - 1]
            ),
            0,
        )

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        nums = list(map(int, input().split()))
        print(Solution().largestPerimeter(nums))
```