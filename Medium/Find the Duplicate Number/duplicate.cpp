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
