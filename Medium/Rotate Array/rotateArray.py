from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for _ in range(k):
            nums.insert(0, nums[-1])
            nums.pop(-1)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        nums = list(map(int, input().strip().split()))
        k = int(input())
        Solution().rotate(nums, k)
        print(nums)
