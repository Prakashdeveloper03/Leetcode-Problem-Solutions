#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    vector<int> nextGreaterElements(vector<int> &nums)
    {
        int n = nums.size();
        vector<int> res(n);
        stack<int> st;
        for (int i = 2 * n - 1; i >= 0; i--)
        {
            while (!st.empty() && st.top() <= nums[i % n])
                st.pop();
            if (i < n)
            {
                if (st.empty())
                    res[i] = -1;
                else
                    res[i] = st.top();
            }
            st.push(nums[i % n]);
        }
        return res;
    }
};

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        vector<int> nums;
        for (int i = 0; i < n; i++)
        {
            int val;
            cin >> val;
            nums.push_back(val);
        }
        Solution obj;
        vector<int> res = obj.nextGreaterElements(nums);
        for (int element : res)
        {
            cout << element << " ";
        }
        cout << endl;
    }
    return 0;
}