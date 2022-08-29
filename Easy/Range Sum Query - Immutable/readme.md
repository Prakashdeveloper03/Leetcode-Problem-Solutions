# Range Sum Query - Immutable
![made-with-Python](https://img.shields.io/badge/Made%20with-Python-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Given an integer array nums, handle multiple queries of the following type:
1. Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

Implement the NumArray class:
- NumArray(int[] nums) Initializes the object with the integer array nums.
- int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

__Example 1:__
```
Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
```

__Constraints:__
- 1 <= nums.length <= 10<sup>4</sup>
- -10<sup>5</sup> <= nums[i] <= 10<sup>5</sup>
- 0 <= left <= right < nums.length
- At most 10<sup>4</sup> calls will be made to sumRange.

  
### Solution
```py
from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        self.left, self.right = left, right
        return sum(self.nums[self.left : self.right + 1])

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        nums = list(map(int, input().split()))
        obj = NumArray(nums)
        n = int(input())
        for _ in range(n):
            left, right = list(map(int, input().split()))
            print(obj.sumRange(left, right))
```