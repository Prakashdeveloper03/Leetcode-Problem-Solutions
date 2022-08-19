#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    int subtractProductAndSum(int num)
    {
        int remainder, product = 1, sum = 0;
        while (num != 0)
        {
            remainder = num % 10;
            product *= remainder;
            sum += remainder;
            num /= 10;
        }
        return product - sum;
    }
};

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int num;
        cin >> num;
        Solution obj;
        cout << obj.subtractProductAndSum(num) << endl;
    }
    return 0;
}