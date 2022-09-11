from typing import List


class Solution:
    def smallestRangeII(self, lis: List[int], k: int) -> int:
        lis.sort()
        ans = lis[-1] - lis[0]
        for i in range(1, len(lis)):
            l = lis[:i]
            r = lis[i:]
            mini = min(l[0] + k, r[0] - k)
            maxi = max(l[-1] + k, r[-1] - k)
            ans = min(ans, maxi - mini)
        return ans


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        lis = list(map(int, input().strip().split()))
        k = int(input())
        print(Solution().smallestRangeII(lis, k))
