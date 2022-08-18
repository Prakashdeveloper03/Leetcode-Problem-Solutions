class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (0 if not low % 2 and not high % 2 else 1) + (high - low) // 2


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        low = int(input())
        high = int(input())
        print(Solution().countOdds(low, high))
