#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
	int maxSubArray(vector<int> &nums)
	{
		int sum = 0;
		int max_sum = INT_MIN;
		for (int i = 0; i < nums.size(); i++)
		{
			sum = sum + nums[i];
			max_sum = max(max_sum, sum);
			if (sum < 0)
				sum = 0;
		}
		return max_sum;
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
		cout << obj.maxSubArray(nums) << endl;
	}
	return 0;
}