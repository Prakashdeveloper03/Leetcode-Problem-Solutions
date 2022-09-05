# Rotate Image
![made-with-Python](https://img.shields.io/badge/Made%20with-Python-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

You are given an `n x n` 2D matrix representing an image, rotate the image by `90` degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. **DO NOT** allocate another 2D matrix and do the rotation.

__Example 1:__
```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
```
__Example 2:__
```
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
```

__Constraints:__
- n == matrix.length == matrix[i].length
- 1 <= n <= 20
- -1000 <= matrix[i][j] <= 1000

### Solution
```py
import itertools
import numpy as np
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rotated = np.rot90(np.array(matrix), -1)
        for i, j in itertools.product(range(rotated.shape[0]), range(rotated.shape[1])):
            matrix[i][j] = rotated[i][j]

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        matrix = list(map(int, input().split()))
        Solution().rotate(matrix)
        print(matrix)
```