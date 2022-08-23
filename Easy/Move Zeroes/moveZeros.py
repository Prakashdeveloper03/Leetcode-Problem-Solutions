from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero = 0
        for idx in range(len(nums)):
            if nums[idx] != 0:
                nums[idx], nums[zero] = nums[zero], nums[idx]
                zero += 1


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        nums = list(map(int, input().split()))
        Solution().moveZeroes(nums)
        print(nums)
