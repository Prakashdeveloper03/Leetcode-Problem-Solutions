#include <bits/stdc++.h>
using namespace std;
class MyQueue
{
public:
    stack<int> s;
    void push(int x)
    {
        if (s.empty())
        {
            s.push(x);
            return;
        }
        int n = s.top();
        s.pop();
        push(x);
        s.push(n);
    }

    int pop()
    {
        int n = s.top();
        s.pop();
        return n;
    }

    int peek()
    {
        return s.top();
    }

    bool empty()
    {
        return s.empty();
    }
};

int main()
{
    MyQueue myQueue;
    myQueue.push(1);
    myQueue.push(2);
    cout << myQueue.peek() << endl;
    cout << myQueue.pop() << endl;
    cout << myQueue.empty() << endl;
    return 0;
}