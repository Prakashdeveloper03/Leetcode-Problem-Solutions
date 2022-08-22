#include <bits\stdc++.h>
using namespace std;
class Solution
{
public:
    vector<int> nextGreaterElement(vector<int> &nums1, vector<int> &nums2)
    {
        stack<int> st;
        vector<int> ans;
        unordered_map<int, int> mp;
        for (int i = nums2.size() - 1; i >= 0; i--)
        {
            if (st.empty())
                mp[nums2[i]] = -1;
            else if (st.top() >= nums2[i])
                mp[nums2[i]] = st.top();
            else
            {
                while (st.size() > 0 and st.top() <= nums2[i])
                    st.pop();
                if (st.size() == 0)
                    mp[nums2[i]] = -1;
                else
                    mp[nums2[i]] = st.top();
            }
            st.push(nums2[i]);
        }
        for (int i = 0; i < nums1.size(); i++)
            ans.push_back(mp[nums1[i]]);
        return ans;
    }
};

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        vector<int> nums1, nums2;
        int l1, l2;
        cin >> l1 >> l2;
        for (int i = 0; i < l1; i++)
        {
            cin >> nums1[i];
        }
        for (int j = 0; j < l2; j++)
        {
            cin >> nums2[j];
        }
        Solution obj;
        vector<int> res = obj.nextGreaterElement(nums1, nums2);
        for (int x : res)
        {
            cout << x << " ";
        }
        cout << endl;
    }
    return 0;
}