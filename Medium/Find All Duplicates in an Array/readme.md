# Find All Duplicates in an Array
![made-with-cpp](https://img.shields.io/badge/Made%20with-C++-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears **once** or **twice**, return an array of all the integers that appears twice. You must write an algorithm that runs in `O(n)` time and uses only constant extra space.

__Example 1:__
```
Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
```
__Example 2:__
```
Input: nums = [1,1,2]
Output: [1]
```

__Example 3:__
```
Input: nums = [1]
Output: []
```

__Constraints:__
- n == nums.length
- 1 <= n <= 10<sup>5</sup>
- 1 <= nums[i] <= n
- Each element in nums appears **once** or **twice**.

### Solution
```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
	vector<int> findDuplicates(vector<int> &nums)
	{
		vector<int> ans;
		for (int i = 0; i < nums.size(); i++)
		{
			int t = abs(nums[i]);
			if (nums[t - 1] > 0)
				nums[t - 1] *= (-1);
			else if (nums[t - 1] < 0)
				ans.push_back(abs(nums[i]));
		}
		return ans;
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
		vector<int> res = obj.findDuplicates(nums);
		for (int element : res)
		{
			cout << element << " ";
		}
		cout << endl;
	}
	return 0;
}
```