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
