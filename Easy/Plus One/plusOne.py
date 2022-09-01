from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nums = int("".join(map(str, digits))) + 1
        return [int(x) for x in str(nums)]


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        digits = list(map(int, input().strip().split()))
        print(Solution().plusOne(digits))
