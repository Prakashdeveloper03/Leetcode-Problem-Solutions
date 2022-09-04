# Daily Temperatures
![made-with-Python](https://img.shields.io/badge/Made%20with-Python-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Given an array of integers temperatures represents the daily temperatures, return an array answer such that `answer[i]` is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

__Example 1:__
```
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
```
__Example 2:__
```
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
```
__Example 3:__
```
Input: temperatures = [30,60,90]
Output: [1,1,0]
```

__Constraints:__
- 1 <= temperatures.length <= 10<sup>5</sup>
- 30 <= temperatures[i] <= 100

### Solution
```py
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = len(temperatures) * [0]
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                result[index] = i - index
            stack.append(i)
        return result

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        temperatures = list(map(int, input().split()))
        print(Solution().dailyTemperatures(temperatures))
```