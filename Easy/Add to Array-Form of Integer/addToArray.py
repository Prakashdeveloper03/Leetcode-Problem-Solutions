from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        l = int("".join([str(i) for i in num]))
        return [int(x) for x in str(l + k)]


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        num = list(map(int, input().split()))
        k = int(input())
        print(Solution().addToArrayForm(num, k))
