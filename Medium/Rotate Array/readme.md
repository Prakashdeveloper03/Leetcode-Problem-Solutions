# Rotate Array
![made-with-Python](https://img.shields.io/badge/Made%20with-Python-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Given an array, rotate the array to the right by `k` steps, where `k` is non-negative.

__Example 1:__
```
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
```
__Example 2:__
```
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
```

__Constraints:__
- 1 <= nums.length <= 10<sup>5</sup>
- -2<sup>31</sup> <= nums[i] <= 2<sup>31</sup> - 1
- 0 <= k <= 10<sup>5</sup>

### Solution
```py
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for _ in range(k):
            nums.insert(0, nums[-1])
            nums.pop(-1)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        nums = list(map(int, input().strip().split()))
        k = int(input())
        Solution().rotate(nums, k)
        print(nums)
```