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