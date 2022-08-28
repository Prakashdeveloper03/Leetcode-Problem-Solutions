# Implement Queue using Stacks
![made-with-cpp](https://img.shields.io/badge/Made%20with-C++-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:
- **void push(int x)** - Pushes element x to the back of the queue.
- **int pop()** - Removes the element from the front of the queue and returns it.
- **int peek()** - Returns the element at the front of the queue.
- **boolean empty()** - Returns true if the queue is empty, false otherwise.

**Notes:**

- You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
- Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.


__Example 1:__
```
Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]

Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
```

__Constraints:__
- 1 <= x <= 9
- At most 100 calls will be made to push, pop, peek, and empty.
- All the calls to pop and peek are valid.


### Solution
```cpp
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
```