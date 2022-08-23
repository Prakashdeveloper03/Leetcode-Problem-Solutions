from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        lengths = [i + 1 for i in range(len(arr)) if i % 2 == 0]
        res = 0
        for l in lengths:
            for i in range(len(arr) + 1 - l):
                res += sum(arr[i : i + l])
        return res


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        print(Solution().sumOddLengthSubarrays(arr))
