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
