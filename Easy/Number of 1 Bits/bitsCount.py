class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(Solution().hammingWeight(n))
