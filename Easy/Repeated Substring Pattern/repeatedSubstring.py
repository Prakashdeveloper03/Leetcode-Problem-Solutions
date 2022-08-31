class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in s[1:] + s[:-1]


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        print(Solution().repeatedSubstringPattern(s))
