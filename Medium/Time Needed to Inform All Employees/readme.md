# Time Needed to Inform All Employees
![made-with-cpp](https://img.shields.io/badge/Made%20with-C++-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

A company has `n` employees with a unique ID for each employee from `0` to `n - 1`. The head of the company is the one with `headID`.

Each employee has one direct manager given in the manager array where manager[i] is the direct manager of the i-th employee, `manager[headID] = -1`. Also, it is guaranteed that the subordination relationships have a tree structure.

The head of the company wants to inform all the company employees of an urgent piece of news. He will inform his direct subordinates, and they will inform their subordinates, and so on until all employees know about the urgent news.

The i-th employee needs `informTime[i]` minutes to inform all of his direct subordinates (i.e., After informTime[i] minutes, all his direct subordinates can start spreading the news).

Return the number of minutes needed to inform all the employees about the urgent news.

__Example 1:__
```
Input: n = 1, headID = 0, manager = [-1], informTime = [0]
Output: 0
Explanation: The head of the company is the only employee in the company.
```
__Example 2:__
```
Input: n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
Output: 1
Explanation: The head of the company with id = 2 is the direct manager of all the employees in the company and needs 1 minute to inform them all.
The tree structure of the employees in the company is shown.
```

__Constraints:__
- 1 <= n <= 10<sup>5</sup>
- 0 <= headID < n
- manager.length == n
- 0 <= manager[i] < n
- manager[headID] == -1
- informTime.length == n
- 0 <= informTime[i] <= 1000
- informTime[i] == 0 if employee i has no subordinates.
- It is guaranteed that all the employees can be informed.


### Solution
```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    int ans = INT_MIN, tmp = 0;
    unordered_map<int, vector<int>> mp;
    vector<int> *pInformTime;
    int numOfMinutes(int n, int headID, vector<int> &manager, vector<int> &informTime)
    {
        pInformTime = &informTime;
        for (int i = 0; i < n; i++)
            mp[manager[i]].push_back(i);
        dfs(headID);
        return ans;
    }
    void dfs(int i)
    {
        if (mp.find(i) == mp.end())
        {
            ans = max(ans, tmp);
        }
        else
        {
            tmp += (*pInformTime)[i];
            for (auto &c : mp[i])
                dfs(c);
            tmp -= (*pInformTime)[i];
        }
    }
};

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, headID;
        cin >> n >> headID;
        int elementCount;
        cin >> elementCount;
        vector<int> manager, informTime;
        for (int i = 0; i < n; i++)
        {
            int val;
            cin >> val;
            manager.push_back(val);
        }
        for (int i = 0; i < n; i++)
        {
            int val;
            cin >> val;
            informTime.push_back(val);
        }
        Solution obj;
        cout << obj.numOfMinutes(n, headID, manager, informTime) << endl;
    }
}
```