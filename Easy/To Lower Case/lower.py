class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        print(Solution().toLowerCase(s))
