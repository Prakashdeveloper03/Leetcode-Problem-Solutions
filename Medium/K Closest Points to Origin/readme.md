# K Closest Points to Origin
![made-with-Python](https://img.shields.io/badge/Made%20with-Python-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Given an array of points where points[i] = [x<sub>i</sub>, y<sub>i</sub>] represents a point on the `X-Y` plane and an integer k, return the `k` closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x<sub>1</sub> - x<sub>2</sub>)<sup>2</sup> + (y<sub>1</sub> - y<sub>2</sub>)<sup>2</sup>).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

__Example 1:__
```
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
```
__Example 2:__
```
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
```

__Constraints:__
- 1 <= k <= points.length <= 10<sup>4</sup>
- -10<sup>4</sup> < xi, yi < 10<sup>4</sup>

### Solution
```py
from typing import List
from heapq import heapify, nsmallest

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [
            (pow(points[i][0], 2) + pow(points[i][1], 2), i) for i in range(len(points))
        ]
        heapify(heap)
        return [points[x[1]] for x in nsmallest(k, heap)]

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        points = []
        for _ in range(n):
            temp = list(map(int, input().strip().split()))
            points.append(temp)
        k = int(input())
        print(Solution().kClosest(points, k))
```