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
