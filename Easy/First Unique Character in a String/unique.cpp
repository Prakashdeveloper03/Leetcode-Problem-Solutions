#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    int firstUniqChar(string s)
    {
        map<char, int> hmap;
        for (int idx{}; idx < s.size(); idx++)
            hmap[s[idx]]++;

        for (int idx{}; idx < s.size(); idx++)
        {
            if (hmap[s[idx]] == 1)
                return idx;
        }
        return -1;
    }
};