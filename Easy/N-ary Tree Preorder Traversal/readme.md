# N-ary Tree Preorder Traversal
![made-with-cpp](https://img.shields.io/badge/Made%20with-C++-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

__Example 1:__
```
Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]
```

__Example 2:__
```
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]
```

__Constraints:__
- The number of nodes in the tree is in the range [0, 10<sup>4</sup>].
- 0 <= Node.val <= 10<sup>4</sup>
- The height of the n-ary tree is less than or equal to 1000


### Solution
```cpp
#include <bits/stdc++.h>
using namespace std;
class Node
{
public:
    int val;
    vector<Node *> children;

    Node() {}

    Node(int _val)
    {
        val = _val;
    }

    Node(int _val, vector<Node *> _children)
    {
        val = _val;
        children = _children;
    }
};

class Solution
{
public:
    void dfs(Node *r, vector<int> &res)
    {
        if (r == NULL)
            return;
        res.push_back(r->val);
        for (auto x : r->children)
            dfs(x, res);
    }
    vector<int> preorder(Node *root)
    {
        vector<int> res;
        dfs(root, res);
        return res;
    }
};
```