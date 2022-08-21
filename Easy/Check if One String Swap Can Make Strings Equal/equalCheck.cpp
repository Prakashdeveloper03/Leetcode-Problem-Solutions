#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    bool areAlmostEqual(string s1, string s2)
    {
        if (s1 == s2)
            return true;
        vector<int> index;
        for (int i = 0; i < s2.length(); i++)
        {
            if (s1[i] != s2[i])
            {
                index.push_back(i);
            }
            if (index.size() > 2)
                return false;
        }
        if (index.size() == 2)
        {
            swap(s2[index[0]], s2[index[1]]);
            return true ? (s1 == s2) : false;
        }
        else
            return false;
    }
};

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        string s1, s2;
        cin >> s1 >> s2;
        Solution obj;
        cout << obj.areAlmostEqual(s1, s2) << endl;
    }
    return 0;
}