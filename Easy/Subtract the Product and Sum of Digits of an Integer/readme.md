# Subtract the Product and Sum of Digits of an Integer
![made-with-cpp](https://img.shields.io/badge/Made%20with-C++-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Given an integer number `n`, return the difference between the product of its digits and the sum of its digits.

__Example 1:__
```
Input: n = 234
Output: 15
Explanation:
Product of digits = 2 * 3 * 4 = 24
Sum of digits = 2 + 3 + 4 = 9
Result = 24 - 9 = 15
```

__Example 2:__
```
Input: n = 4421
Output: 21
Explanation:
Product of digits = 4 * 4 * 2 * 1 = 32
Sum of digits = 4 + 4 + 2 + 1 = 11
Result = 32 - 11 = 21
```

__Constraints:__
- 1 <= n <= 10^5

### Solution
```cpp
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
```