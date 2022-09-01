# Evaluate Reverse Polish Notation
![made-with-cpp](https://img.shields.io/badge/Made%20with-C++-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

**Note:** that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.

__Example 1:__
```
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
```
__Example 2:__
```
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
```
__Example 3:__
```
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
```

__Constraints:__
- 1 <= tokens.length <= 10<sup>4</sup>
- tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].

### Solution
```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    int evalRPN(vector<string> &tokens)
    {
        stack<int> st;
        for (int i = 0; i < tokens.size(); i++)
        {
            if (tokens[i] == "+")
            {
                int operand2 = st.top();
                st.pop();
                int operand1 = st.top();
                st.pop();
                st.push(operand1 + operand2);
            }
            else if (tokens[i] == "-")
            {
                int operand2 = st.top();
                st.pop();
                int operand1 = st.top();
                st.pop();
                st.push(operand1 - operand2);
            }
            else if (tokens[i] == "*")
            {
                int operand2 = st.top();
                st.pop();
                int operand1 = st.top();
                st.pop();
                st.push(operand1 * operand2);
            }
            else if (tokens[i] == "/")
            {
                int operand2 = st.top();
                st.pop();
                int operand1 = st.top();
                st.pop();
                st.push(operand1 / operand2);
            }
            else
            {
                st.push(stoi(tokens[i]));
            }
        }
        return st.top();
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
        vector<string> tokens;
        for (int i = 0; i < n; i++)
        {
            string val;
            cin >> val;
            tokens.push_back(val);
        }
        Solution obj;
        cout << obj.evalRPN(tokens) << endl;
    }
    return 0;
}
```