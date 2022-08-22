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