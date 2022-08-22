# Next Greater Element I
![made-with-cpp](https://img.shields.io/badge/Made%20with-C++-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

The next greater element of some element x in an array is the first greater element that is to the right of `x` in the same array.

You are given two distinct **0-indexed integer arrays** `nums1` and `nums2`, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

__Example 1:__
```
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
```

__Example 2:__
```
Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
```

__Constraints:__
- 1 <= nums1.length <= nums2.length <= 1000
- 0 <= nums1[i], nums2[i] <= 10<sup>4</sup>
- All integers in nums1 and nums2 are unique.
- All the integers of nums1 also appear in nums2.


### Solution
```cpp
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
```