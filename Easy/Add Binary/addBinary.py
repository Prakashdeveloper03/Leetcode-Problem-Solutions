class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a, b = input().split()
        print(Solution().addBinary(a, b))
