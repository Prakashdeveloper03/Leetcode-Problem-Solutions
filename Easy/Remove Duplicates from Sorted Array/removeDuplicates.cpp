#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
	int removeDuplicates(vector<int> &nums)
	{
		int j = 0;
		unordered_map<int, int> m;
		int counter = 0;
		for (int i = 0; i < nums.size(); i++)
		{
			if (m[nums[i]] == 0)
			{
				m[nums[i]]++;
				nums[j] = nums[i];
				j++;
				counter++;
			}
		}
		return counter;
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
		cout << obj.removeDuplicates(nums) << endl;
	}
	return 0;
}