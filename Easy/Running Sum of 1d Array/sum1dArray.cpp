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