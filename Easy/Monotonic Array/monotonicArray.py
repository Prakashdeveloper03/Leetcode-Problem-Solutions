from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        return nums in [sorted(nums), sorted(nums, reverse=True)]


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        nums = list(map(int, input().strip().split()))
        print(Solution().isMonotonic(nums))
