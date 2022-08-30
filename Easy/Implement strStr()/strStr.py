class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        haystack, needle = input().strip().split()
        print(Solution().strStr(haystack, needle))
