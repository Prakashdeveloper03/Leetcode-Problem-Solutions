# Lemonade Change
![made-with-Python](https://img.shields.io/badge/Made%20with-Python-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

At a lemonade stand, each lemonade costs `$5`. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a `$5`, `$10`, or `$20` bill. You must provide the correct change to each customer so that the net transaction is that the customer pays `$5`.

Note that you do not have any change in hand at first.

Given an integer array `bills` where `bills[i]` is the bill the ith customer pays, return **true** if you can provide every customer with the correct change, or **false** otherwise.

__Example 1:__
```
Input: bills = [5,5,5,10,20]
Output: true
Explanation:
From the first 3 customers, we collect three $5 bills in order.
From the fourth customer, we collect a $10 bill and give back a $5.
From the fifth customer, we give a $10 bill and a $5 bill.
Since all customers got correct change, we output true.
```
__Example 2:__
```
Input: bills = [5,5,10,10,20]
Output: false
Explanation:
From the first two customers in order, we collect two $5 bills.
For the next two customers in order, we collect a $10 bill and give back a $5 bill.
For the last customer, we can not give the change of $15 back because we only have two $10 bills.
Since not every customer received the correct change, the answer is false.
```

__Constraints:__
- 1 <= bills.length <= 10<sup>5</sup>
- bills[i] is either 5, 10, or 20.

### Solution
```py
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
```