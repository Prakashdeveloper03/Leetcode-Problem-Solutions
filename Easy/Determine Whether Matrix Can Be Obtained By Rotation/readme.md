# Determine Whether Matrix Can Be Obtained By Rotation
![made-with-Python](https://img.shields.io/badge/Made%20with-Python-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Given two `n x n` binary matrices mat and target, return true if it is possible to make mat equal to target by rotating mat in **90-degree increments**, or false otherwise.

__Example 1:__
```
Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise to make mat equal target.
```
__Example 2:__
```
Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
Output: false
Explanation: It is impossible to make mat equal to target by rotating mat.
```
__Example 3:__
```
Input: mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise two times to make mat equal target.
```

__Constraints:__
- n == mat.length == target.length
- n == mat[i].length == target[i].length
- 1 <= n <= 10
- mat[i][j] and target[i][j] are either 0 or 1.
  
### Solution
```py
from typing import List

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if target == mat:
            return True
        for _ in range(3, 0, -1):
            n = len(mat)
            mat2 = []
            for j in range(n):
                temp = []
                i = n - 1
                while i >= 0:
                    temp.append(mat[i][j])
                    i -= 1
                mat2.append(temp)
            if mat2 == target:
                return True
            else:
                mat = mat2
        return False

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        mat = []
        target = []
        for _ in range(n):
            temp = list(map(int, input().split()))
            mat.append(temp)
        for _ in range(n):
            temp = list(map(int, input().split()))
            target.append(temp)
        print(Solution().findRotation(mat, target))
```