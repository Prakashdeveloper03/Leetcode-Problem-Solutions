# Check If It Is a Straight Line
![made-with-cpp](https://img.shields.io/badge/Made%20with-C++-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

You are given an array `coordinates`, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

__Example 1:__
```
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
```

__Example 2:__
```
Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false
```

__Constraints:__
- 2 <= coordinates.length <= 1000
- coordinates[i].length == 2
- -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
- coordinates contains no duplicate point.


### Solution
```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    bool checkStraightLine(vector<vector<int>> &coordinates)
    {
        int x, y;
        if (coordinates.size() == 2)
            return true;
        int x0 = coordinates[0][0], x1 = coordinates[1][0];
        int y0 = coordinates[0][1], y1 = coordinates[1][1];
        int dx = x1 - x0, dy = y1 - y0;
        for (int i = 2; i < coordinates.size(); i++)
        {
            x = coordinates[i][0];
            y = coordinates[i][1];
            if (dy * (x - x0) != dx * (y - y0))
                return false;
        }
        return true;
    }
};
```