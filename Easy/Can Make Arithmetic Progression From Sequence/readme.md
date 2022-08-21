# Can Make Arithmetic Progression From Sequence
![made-with-cpp](https://img.shields.io/badge/Made%20with-C++-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

A sequence of numbers is called an **arithmetic progression** if the difference between any two consecutive elements is the same.

Given an array of numbers `arr`, return `true` if the array can be rearranged to form an arithmetic progression. Otherwise, return `false`.

__Example 1:__
```
Input: arr = [3,5,1]
Output: true
Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.
```

__Example 2:__
```
Input: arr = [1,2,4]
Output: false
Explanation: There is no way to reorder the elements to obtain an arithmetic progression.
```

__Constraints:__
- 2 <= arr.length <= 1000
- -10<sup>6</sup> <= arr[i] <= 10<sup>6</sup>


### Solution
```cpp
#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    bool canMakeArithmeticProgression(vector<int> &arr)
    {
        int difference, current_difference;
        sort(arr.begin(), arr.end());
        difference = arr[1] - arr[0];
        for (int itr = 0; itr < arr.size() - 1; itr++)
        {
            current_difference = arr[itr + 1] - arr[itr];
            if (current_difference != difference)
                return false;
        }
        return true;
    }
};

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        vector<int> arr;
        int length, value;
        cin >> length;
        for (int i = 0; i < length; i++)
        {
            cin >> value;
            arr.push_back(value);
        }
        Solution obj;
        cout << obj.canMakeArithmeticProgression(arr) << endl;
    }
    return 0;
}
```