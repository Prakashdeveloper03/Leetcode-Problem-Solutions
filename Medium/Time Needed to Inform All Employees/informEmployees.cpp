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
