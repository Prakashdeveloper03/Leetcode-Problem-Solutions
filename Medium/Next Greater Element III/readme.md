# Next Greater Element III
![made-with-cpp](https://img.shields.io/badge/Made%20with-C++-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Given a positive integer `n`, find the smallest integer which has exactly the same digits existing in the integer `n` and is greater in value than `n`. If no such positive integer exists, return `-1`.

Note that the returned integer should fit in **32-bit integer**, if there is a valid answer but it does not fit in **32-bit integer**, return `-1`.

__Example 1:__
```
Input: n = 12
Output: 21
```
__Example 2:__
```
Input: n = 21
Output: -1
```

__Constraints:__
- 1 <= n <= 2<sup>31</sup> - 1

### Solution
```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    int nextGreaterElement(int num)
    {
        string s = to_string(num);
        int n = s.length();
        int right = n - 1, left = n - 2;
        int index;
        while (left >= 0)
        {
            if (s[left] >= s[right])
            {
                left--;
                right--;
            }
            else
            {
                index = right;
                while (right < n)
                {
                    if (s[right] > s[left])
                        index = right;
                    right++;
                }
                break;
            }
        }
        if (left == -1)
            return -1;
        swap(s[left], s[index]);
        sort(s.begin() + left + 1, s.end());
        long long ans = stoll(s);
        if (ans <= pow(2, 31) - 1)
            return stoi(s);
        else
            return -1;
    }
};

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int num;
        cin >> num;
        Solution obj;
        cout << obj.nextGreaterElement(num) << endl;
    }
    return 0;
}
```