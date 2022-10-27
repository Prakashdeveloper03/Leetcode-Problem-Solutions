from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target not in nums:
            nums.append(target)
            nums.sort()
        return nums.index(target)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        nums = list(map(int, input().strip().split()))
        target = int(input())
        print(Solution().searchInsert(nums, target))
