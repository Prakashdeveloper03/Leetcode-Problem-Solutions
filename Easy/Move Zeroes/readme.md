# Move Zeroes
![made-with-Python](https://img.shields.io/badge/Made%20with-Python-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

**Note** that you must do this in-place without making a copy of the array.

__Example 1:__
```
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
```
__Example 2:__
```
Input: nums = [0]
Output: [0]
```

__Constraints:__
- 1 <= nums.length <= 10<sup>4</sup>
- -2<sup>31</sup> <= nums[i] <= 2<sup>31</sup> - 1

### Solution
```py
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero = 0
        for idx in range(len(nums)):
            if nums[idx] != 0:
                nums[idx], nums[zero] = nums[zero], nums[idx]
                zero += 1

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        nums = list(map(int, input().split()))
        Solution().moveZeroes(nums)
        print(nums)
```