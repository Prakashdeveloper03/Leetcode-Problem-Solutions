# Basic Calculator
![made-with-C++](https://img.shields.io/badge/Made%20with-C++-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

**Note:** You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

__Example 1:__
```
Input: s = "1 + 1"
Output: 2
```
__Example 2:__
```
Input: s = " 2-1 + 2 "
Output: 3
```

__Example 3:__
```
Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
```

__Constraints:__
- 1 <= s.length <= 3 * 10<sup>5</sup>
- s consists of digits, '+', '-', '(', ')', and ' '.
- s represents a valid expression.
- '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
- '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
- There will be no two consecutive operators in the input.
- Every number and running calculation will fit in a signed 32-bit integer


### Solution
```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution
{
private:
    int i = 0;

public:
    int calculate(string s)
    {
        vector<int> stk;
        char sign = '+';
        int num = 0;
        while (i < s.size())
        {
            char ch = s[i++];
            if (isdigit(ch))
            {
                num = num * 10 + (ch - '0');
            }
            if (ch == '(')
                num = calculate(s);
            if (i >= s.size() || ch == '+' || ch == '-' || ch == ')')
            {
                if (sign == '+')
                    stk.push_back(num);
                else
                    stk.push_back(-num);
                sign = ch;
                num = 0;
            }
            if (ch == ')')
                break;
        }
        return accumulate(stk.begin(), stk.end(), 0);
    }
};

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        string s;
        getline(cin, s);
        Solution obj;
        cout << obj.calculate(s) << endl;
    }
    return 0;
}
```

