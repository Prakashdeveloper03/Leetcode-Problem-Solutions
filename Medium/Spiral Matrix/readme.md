# Spiral Matrix
![made-with-Python](https://img.shields.io/badge/Made%20with-Python-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Given an `m x n` matrix, return all elements of the matrix in **spiral order**.

__Example 1:__
```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
```
__Example 2:__
```
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

__Constraints:__
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 10
- -100 <= matrix[i][j] <= 100

### Solution
```py
import numpy as np
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        while matrix:
            result += matrix[0]
            matrix = np.transpose(matrix[1:])[::-1].tolist()
        return result

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        matrix = []
        for _ in range(n):
            temp = list(map(int, input().strip().split()))
            matrix.append(temp)
        print(Solution().spiralOrder(matrix))
```