# Richest Customer Wealth
![made-with-Python](https://img.shields.io/badge/Made%20with-Python-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

You are given an m x n integer grid `accounts` where `accounts[i][j]` is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

__Example 1:__
```
Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
Explanation:
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Both customers are considered the richest with a wealth of 6 each, so return 6.
```
__Example 2:__
```
Input: accounts = [[1,5],[7,3],[3,5]]
Output: 10
Explanation:
1st customer has wealth = 6
2nd customer has wealth = 10
3rd customer has wealth = 8
The 2nd customer is the richest with a wealth of 10.
```
__Example 3:__
```
Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]
Output: 17
```

__Constraints:__
- m == accounts.length
- n == accounts[i].length
- 1 <= m, n <= 50
- 1 <= accounts[i][j] <= 100

### Solution
```py
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
```