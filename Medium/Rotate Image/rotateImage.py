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
