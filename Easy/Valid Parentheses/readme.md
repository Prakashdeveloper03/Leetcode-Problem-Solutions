# Valid Parentheses
![made-with-cpp](https://img.shields.io/badge/Made%20with-C++-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.

__Example 1:__
```
Input: s = "()"
Output: true
```

__Example 2:__
```
Input: s = "()[]{}"
Output: true
```

__Example 3:__
```
Input: s = "(]"
Output: false
```

__Constraints:__
- 1 <= s.length <= 10<sup>4</sup>
- s consists of parentheses only '()[]{}'.

### Solution
```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    bool isValid(string s)
    {
        stack<char> st;
        for (auto i : s)
        {
            if (st.empty() && (i == ')' || i == ']' || i == '}'))
            {
                return false;
            }
            else if (i == '(' || i == '[' || i == '{')
            {
                st.push(i);
            }
            else if (!st.empty() && st.top() == '[' && i == ']')
            {
                st.pop();
            }
            else if (!st.empty() && st.top() == '(' && i == ')')
            {
                st.pop();
            }
            else if (!st.empty() && st.top() == '{' && i == '}')
            {
                st.pop();
            }
            else
                return false;
        }
        if (st.size() == 0)
            return true;
        return false;
    }
};

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        string s;
        cin >> s;
        Solution obj;
        cout << obj.isValid(s) << endl;
    }
    return 0;
}
```