# Add to Array-Form of Integer
![made-with-Python](https://img.shields.io/badge/Made%20with-Python-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

The **array-form** of an integer num is an array representing its digits in left to right order.

- For example, for num = `1321`, the array form is `[1,3,2,1]`.

Given num, the **array-form** of an integer, and an integer `k`, return the array-form of the integer num + k.


__Example 1:__
```
Input: num = [1,2,0,0], k = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234
```
__Example 2:__
```
Input: num = [2,7,4], k = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455
```
__Example 3:__
```
Input: num = [2,1,5], k = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021
```

__Constraints:__
- 1 <= num.length <= 10<sup>4</sup>
- 0 <= num[i] <= 9
- num does not contain any leading zeros except for the zero itself.
- 1 <= k <= 10<sup>4</sup>


### Solution
```py
from typing import List

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        l = int("".join([str(i) for i in num]))
        return [int(x) for x in str(l + k)]

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        num = list(map(int, input().split()))
        k = int(input())
        print(Solution().addToArrayForm(num, k))
```