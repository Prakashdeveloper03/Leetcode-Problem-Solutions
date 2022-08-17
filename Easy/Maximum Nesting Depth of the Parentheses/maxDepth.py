from operator import add
from itertools import accumulate


class Solution:
    def maxDepth(self, s: str) -> int:
        s = "".join((filter(lambda x: x in ["(", ")"], s)))
        if not s:
            return 0
        chars = [1 if ch == "(" else -1 for ch in s]
        return max(accumulate(chars, add))


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        print(Solution().maxDepth(s))
