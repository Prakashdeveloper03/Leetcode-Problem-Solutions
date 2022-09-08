# Next Greater Element II
![made-with-cpp](https://img.shields.io/badge/Made%20with-C++-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Given a circular integer array nums (i.e., the next element of `nums[nums.length - 1]` is nums[0]), return the next greater number for every element in nums.

The **next greater number** of a number `x` is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return `-1` for this number.

__Example 1:__
```
Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2;
The number 2 can't find next greater number.
The second 1's next greater number needs to search circularly, which is also 2.
```
__Example 2:__
```
Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]
```

__Constraints:__
- 1 <= nums.length <= 10<sup>4</sup>
- -10<sup>9</sup> <= nums[i] <= 10<sup>9</sup>


### Solution
```cpp
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
```