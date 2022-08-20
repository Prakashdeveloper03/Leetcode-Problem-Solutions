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