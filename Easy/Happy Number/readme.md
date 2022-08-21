# Happy Number
![made-with-cpp](https://img.shields.io/badge/Made%20with-C++-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Write an algorithm to determine if a number `n` is happy.

A **happy number** is a number defined by the following process:
- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it **loops endlessly in a cycle** which does not include 1.
- Those numbers for which this process ends in 1 are happy.


Return `true` if n is a happy number, and `false` if not.

__Example 1:__
```
Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
```

__Example 2:__
```
Input: n = 2
Output: false
```

__Constraints:__
- 1 <= n <= 2<sup>31</sup> - 1


### Solution
```cpp
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
```