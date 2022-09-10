from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i, j = 0, 0
        mult = 1
        res = 0
        while mult < k and i < len(nums):
            mult *= nums[i]
            i += 1
            while mult >= k:
                mult /= nums[j]
                j += 1
            res += i - j
        return res


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        nums = list(map(int, input().strip().split()))
        k = int(input())
        print(Solution().numSubarrayProductLessThanK(nums, k))
