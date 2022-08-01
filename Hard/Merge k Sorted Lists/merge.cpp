#include <bits/stdc++.h>
using namespace std;
struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution
{
public:
    ListNode *mergeKLists(vector<ListNode *> &lists)
    {
        vector<int> a;
        ListNode *ans = new ListNode();
        ListNode *cur = ans;
        for (int i = 0; i < lists.size(); i++)
        {
            ListNode *curList = lists[i];
            ListNode *node = curList;
            while (node != NULL)
            {
                a.push_back(node->val);
                node = node->next;
            }
        }
        sort(a.begin(), a.end());
        for (int x : a)
        {
            ans->next = new ListNode(x);
            ans = ans->next;
        }
        return cur->next;
    }
};