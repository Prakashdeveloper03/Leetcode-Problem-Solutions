from typing import List


class Solution:
    def checkArithmeticSubarrays(
        self, nums: List[int], l: List[int], r: List[int]
    ) -> List[bool]:
        ans = [True] * len(l)
        for i in range(len(l)):
            test = sorted(nums[l[i] : r[i] + 1])
            dif = test[1] - test[0]
            for j in range(len(test) - 1):
                if test[j + 1] - test[j] != dif:
                    ans[i] = False
                    break
        return ans


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        nums = list(map(int, input().split()))
        l = list(map(int, input().split()))
        r = list(map(int, input().split()))
        print(Solution().checkArithmeticSubarrays(nums, l, r))
