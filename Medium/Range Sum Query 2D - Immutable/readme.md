# Range Sum Query 2D - Immutable
![made-with-Python](https://img.shields.io/badge/Made%20with-Python-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Given a 2D matrix matrix, handle multiple queries of the following type:

- Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Implement the NumMatrix class:

- **NumMatrix(int[][] matrix)** Initializes the object with the integer matrix matrix.
- int **sumRegion(int row1, int col1, int row2, int col2)** Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

You must design an algorithm where sumRegion works on O(1) time complexity.

__Example 1:__
```
Input
["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
Output
[null, 8, 11, 12]

Explanation
NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)
```

__Constraints:__
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 200
- -10<sup>4</sup> <= matrix[i][j] <= 10<sup>4</sup>
- 0 <= row1 <= row2 < m
- 0 <= col1 <= col2 < n
- At most 10<sup>4</sup> calls will be made to sumRegion

### Solution
```py
from typing import List

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.sum = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for r in range(1, m + 1):
            for c in range(1, n + 1):
                self.sum[r][c] = (
                    self.sum[r - 1][c]
                    + self.sum[r][c - 1]
                    - self.sum[r - 1][c - 1]
                    + matrix[r - 1][c - 1]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        return (
            self.sum[r2][c2]
            - self.sum[r1 - 1][c2]
            - self.sum[r2][c1 - 1]
            + self.sum[r1 - 1][c1 - 1]
        )
```