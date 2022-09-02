# Multiply Strings
![made-with-Python](https://img.shields.io/badge/Made%20with-Python-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Given two non-negative integers `num1` and `num2` represented as strings, return the product of num1 and num2, also represented as a string.

**Note:** You must not use any built-in BigInteger library or convert the inputs to integer directly.

__Example 1:__
```
Input: num1 = "2", num2 = "3"
Output: "6"
```
__Example 2:__
```
Input: num1 = "123", num2 = "456"
Output: "56088"
```

__Constraints:__
- 1 <= num1.length, num2.length <= 200
- num1 and num2 consist of digits only.
- Both num1 and num2 do not contain any leading zero, except the number 0 itself.

### Solution
```py
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        digit_map = {
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "0": 0,
        }
        convert = lambda num: sum(
            digit_map[num[i - 1]] * 10 ** (len(num) - i) for i in range(len(num), 0, -1)
        )
        return str(convert(num1) * convert(num2))

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        num1, num2 = input().split()
        print(Solution().multiply(num1, num2))
```