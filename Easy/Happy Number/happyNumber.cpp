#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    int squareDigits(int num)
    {
        int sum = 0;
        while (num != 0)
        {
            int digit = num % 10;
            sum += digit * digit;
            num /= 10;
        }
        return sum;
    }

    bool isHappy(int n)
    {
        int num = 0;
        int itr = 31;
        num = squareDigits(n);
        while (itr--)
        {
            num = squareDigits(num);
            if (num == 1)
                return true;
        }
        return false;
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
        Solution obj;
        cout << obj.isHappy(n) << endl;
    }
    return 0;
}