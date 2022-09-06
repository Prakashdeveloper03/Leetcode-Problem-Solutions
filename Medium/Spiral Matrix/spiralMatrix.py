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
