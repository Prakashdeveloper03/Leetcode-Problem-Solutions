from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        self.left, self.right = left, right
        return sum(self.nums[self.left : self.right + 1])


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        nums = list(map(int, input().split()))
        obj = NumArray(nums)
        n = int(input())
        for _ in range(n):
            left, right = list(map(int, input().split()))
            print(obj.sumRange(left, right))
