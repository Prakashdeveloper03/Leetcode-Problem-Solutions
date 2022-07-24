# Running Sum of 1d Array
![made-with-cpp](https://img.shields.io/badge/Made%20with-C++-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Given an array `nums`. We define a running sum of an array as `runningSum[i] = sum(nums[0]…nums[i])`.
Return the running sum of `nums`.

__Example 1:__
```
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4]
```

__Example 2:__
```
Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
```

__Example 3:__
```
Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
```

__Constraints:__
- 1 <= nums.length <= 1000
- -10^6 <= nums[i] <= 10^6

### Solution
```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
	vector<int> runningSum(vector<int> &nums)
	{
		vector<int> res;
		int sum = 0;
		for (int i = 0; i < nums.size(); i++)
		{
			sum += nums[i];
			res.push_back(sum);
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
		vector<int> res = obj.runningSum(nums);
		for (int val : res)
			cout << val << " ";
		cout << endl;
	}
	return 0;
}
```