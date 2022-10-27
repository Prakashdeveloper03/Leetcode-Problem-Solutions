# Search Insert Position
![made-with-Python](https://img.shields.io/badge/Made%20with-Python-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with `O(log n)` runtime complexity.

__Example 1:__
```
Input: nums = [1,3,5,6], target = 5
Output: 2
```
__Example 2:__
```
Input: nums = [1,3,5,6], target = 2
Output: 1
```
__Example 3:__
```
Input: nums = [1,3,5,6], target = 7
Output: 4
```

__Constraints:__
- 1 <= nums.length <= 10<sup>4</sup>
- -10<sup>4</sup> <= nums[i] <= 10<sup>4</sup>
- `nums` contains distinct values sorted in **ascending order**.
- -10<sup>4</sup> <= target <= 10<sup>4</sup>


### Solution
```py
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target not in nums:
            nums.append(target)
            nums.sort()
        return nums.index(target)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        nums = list(map(int, input().strip().split()))
        target = int(input())
        print(Solution().searchInsert(nums, target))
```