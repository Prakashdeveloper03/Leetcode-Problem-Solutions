# Find Nearest Point That Has the Same X or Y Coordinate
![made-with-cpp](https://img.shields.io/badge/Made%20with-C++-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

You are given two integers, x and y, which represent your current location on a Cartesian grid: (x, y). You are also given an array points where each points[i] = [ai, bi] represents that a point exists at (ai, bi). A point is valid if it shares the same x-coordinate or the same y-coordinate as your location.

Return the index (0-indexed) of the valid point with the smallest Manhattan distance from your current location. If there are multiple, return the valid point with the smallest index. If there are no valid points, return -1.

The Manhattan distance between two points (x1, y1) and (x2, y2) is abs(x1 - x2) + abs(y1 - y2).

__Example 1:__
```
Input: x = 3, y = 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
Output: 2
Explanation: Of all the points, only [3,1], [2,4] and [4,4] are valid. Of the valid points, [2,4] and [4,4] have the smallest Manhattan distance from your current location, with a distance of 1. [2,4] has the smallest index, so return 2.
```

__Example 2:__
```
Input: x = 3, y = 4, points = [[3,4]]
Output: 0
Explanation: The answer is allowed to be on the same location as your current location.
```

__Example 3:__
```
Input: x = 3, y = 4, points = [[2,3]]
Output: -1
Explanation: There are no valid points.
```

__Constraints:__
- 1 <= points.length <= 10<sup>4</sup>
- points[i].length == 2
- 1 <= x, y, ai, bi <= 10<sup>4</sup>


### Solution
```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    int nearestValidPoint(int x, int y, vector<vector<int>> &points)
    {
        int minimum = numeric_limits<int>::max();
        int index = -1;
        int distance;
        for (int i = 0; i < points.size(); i++)
        {
            if (x == points[i][0] || y == points[i][1])
            {
                distance = abs(x - points[i][0]) + abs(y - points[i][1]);
                if (minimum > distance)
                {
                    minimum = distance;
                    index = i;
                }
            }
        }
        return index;
    }
};
```