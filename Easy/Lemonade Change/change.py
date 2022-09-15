from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {5: 0, 10: 0}
        for i in bills:
            if i == 10:
                if change[5] <= 0:
                    return False
                change[5] -= 1
                change[10] += 1
            elif i == 5:
                change[5] += 1
            elif (change[10] > 0) & (change[5] > 0):
                change[10] -= 1
                change[5] -= 1
            elif change[5] >= 3:
                change[5] -= 3
            else:
                return False
        return True


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        bills = list(map(int, input().strip().split()))
        print(Solution().lemonadeChange(bills))
