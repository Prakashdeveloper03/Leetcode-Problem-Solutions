from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return next(iter(Counter(t) - Counter(s)))


if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        s = input()
        t = input()
        print(Solution().findTheDifference(s, t))
