# Find the Duplicate Number
![made-with-cpp](https://img.shields.io/badge/Made%20with-C++-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Given an array of integers nums containing `n + 1` integers where each integer is in the range [1, n] inclusive. There is **only one repeated number** in nums, return this repeated number. You must solve the problem without modifying the array nums and uses only constant extra space.

__Example 1:__
```
Input: nums = [1,3,4,2,2]
Output: 2
```
__Example 2:__
```
Input: nums = [3,1,3,4,2]
Output: 3
```

__Constraints:__
- 1 <= n <= 10<sup>5</sup>
- nums.length == n + 1
- 1 <= nums[i] <= n
- All the integers in nums appear only **once** except for **precisely one integer** which appears two or more times.

### Solution
```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
	int findDuplicate(vector<int> &nums)
	{
		for (int i = 0; i < nums.size(); i++)
		{
			if (nums[abs(nums[i])] > 0)
				nums[abs(nums[i])] = -nums[abs(nums[i])];
			else
				return abs(nums[i]);
		}
		return -1;
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
		cout << obj.findDuplicate(nums) << endl;
	}
	return 0;
}
```