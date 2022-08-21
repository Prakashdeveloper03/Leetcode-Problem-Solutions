# Sign of the Product of an Array
![made-with-Python](https://img.shields.io/badge/Made%20with-Python-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

You are given an integer array `nums`. Let product be the **product** of all values in the array nums.

return sign of the product :
- 1 if x is positive.
- -1 if x is negative.
- 0 if x is equal to 0.

__Example 1:__
```
Input: nums = [-1,-2,-3,-4,3,2,1]
Output: 1
Explanation: The product of all values in the array is 144, and signFunc(144) = 1
```
__Example 2:__
```
Input: nums = [1,5,0,2,-3]
Output: 0
Explanation: The product of all values in the array is 0, and signFunc(0) = 0
```
__Example 3:__
```
Input: nums = [-1,1,-1,1,-1]
Output: -1
Explanation: The product of all values in the array is -1, and signFunc(-1) = -1
```

__Constraints:__
- 1 <= nums.length <= 1000
- -100 <= nums[i] <= 100

### Solution
```py
import math
from typing import List

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = math.prod(nums)
        return 1 if product > 0 else -1 if product < 0 else 0

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        nums = list(map(int, input().split()))
        print(Solution().arraySign(nums))
```