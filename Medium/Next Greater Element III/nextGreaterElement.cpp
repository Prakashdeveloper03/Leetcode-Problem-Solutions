#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    int nextGreaterElement(int num)
    {
        string s = to_string(num);
        int n = s.length();
        int right = n - 1, left = n - 2;
        int index;
        while (left >= 0)
        {
            if (s[left] >= s[right])
            {
                left--;
                right--;
            }
            else
            {
                index = right;
                while (right < n)
                {
                    if (s[right] > s[left])
                        index = right;
                    right++;
                }
                break;
            }
        }
        if (left == -1)
            return -1;
        swap(s[left], s[index]);
        sort(s.begin() + left + 1, s.end());
        long long ans = stoll(s);
        if (ans <= pow(2, 31) - 1)
            return stoi(s);
        else
            return -1;
    }
};

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int num;
        cin >> num;
        Solution obj;
        cout << obj.nextGreaterElement(num) << endl;
    }
    return 0;
}