from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = [sum(x) for x in accounts]
        return max(res)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        accounts = []
        for _ in range(n):
            account = list(map(int, input().split()))
            accounts.append(account)
        print(Solution().maximumWealth(accounts))
