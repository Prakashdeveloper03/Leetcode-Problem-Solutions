#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    bool canMakeArithmeticProgression(vector<int> &arr)
    {
        int difference, current_difference;
        sort(arr.begin(), arr.end());
        difference = arr[1] - arr[0];
        for (int itr = 0; itr < arr.size() - 1; itr++)
        {
            current_difference = arr[itr + 1] - arr[itr];
            if (current_difference != difference)
                return false;
        }
        return true;
    }
};

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        vector<int> arr;
        int length, value;
        cin >> length;
        for (int i = 0; i < length; i++)
        {
            cin >> value;
            arr.push_back(value);
        }
        Solution obj;
        cout << obj.canMakeArithmeticProgression(arr) << endl;
    }
    return 0;
}