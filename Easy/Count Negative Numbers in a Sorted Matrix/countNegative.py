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
