#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
	vector<int> buildArray(vector<int> &nums)
	{
		vector<int> res;
		for (int idx = 0; idx < nums.size(); idx++)
		{
			res.push_back(nums[nums[idx]]);
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
		vector<int> res = obj.buildArray(nums);
		for (int val : res)
			cout << val << " ";
		cout << endl;
	}
	return 0;
}