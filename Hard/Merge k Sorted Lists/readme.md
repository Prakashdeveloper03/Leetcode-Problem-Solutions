# Merge k Sorted Lists
![made-with-C++](https://img.shields.io/badge/Made%20with-C++-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

__Example 1:__
```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
```
__Example 2:__
```
Input: lists = []
Output: []
```

__Example 3:__
```
Input: lists = [[]]
Output: []
```

__Constraints:__
- k == lists.length
- 0 <= k <= 10<sup>4</sup>
- 0 <= lists[i].length <= 500
- -10<sup>4</sup> <= lists[i][j] <= 10<sup>4</sup>
- lists[i] is sorted in ascending order.
- The sum of lists[i].length will not exceed 10<sup>4</sup>.


### Solution
```cpp
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
```

