# Count Negative Numbers in a Sorted Matrix
![made-with-Python](https://img.shields.io/badge/Made%20with-Python-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Given a `m x n` matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in `grid`.

__Example 1:__
```
Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
```
__Example 2:__
```
Input: grid = [[3,2],[1,0]]
Output: 0
```

__Constraints:__
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 100
- -100 <= grid[i][j] <= 100


### Solution
```py
from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum(i < 0 for j in grid for i in j)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        m = int(input())
        grid = []
        for _ in range(n):
            nums = list(map(int, input().strip().split()))
            grid.append(nums)
        print(Solution().countNegatives(grid))
```