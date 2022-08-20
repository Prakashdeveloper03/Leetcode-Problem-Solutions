from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        return next(
            (
                sum(nums[idx - 3 : idx])
                for idx in range(3, len(nums) + 1)
                if nums[idx - 3] < nums[idx - 2] + nums[idx - 1]
            ),
            0,
        )


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        nums = list(map(int, input().split()))
        print(Solution().largestPerimeter(nums))
