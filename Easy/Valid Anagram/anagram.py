from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        t = input()
        print(Solution().isAnagram(s, t))
