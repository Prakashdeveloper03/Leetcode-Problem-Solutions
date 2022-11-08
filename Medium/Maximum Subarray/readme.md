# Maximum Subarray
![made-with-cpp](https://img.shields.io/badge/Made%20with-C++-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/Sublime_Text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Given an integer array `nums`, find the subarray which has the largest `sum` and return its `sum`.

__Example 1:__
```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```
__Example 2:__
```
Input: nums = [1]
Output: 1
```
__Example 3:__
```
Input: nums = [5,4,-1,7,8]
Output: 23
```

__Constraints:__
- 1 <= nums.length <= 10<sup>5</sup>
- -10<sup>4</sup> <= nums[i] <= 10<sup>4</sup>

### Solution
```cpp
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int sum = 0;
        int max_sum = INT_MIN;
        for(int i = 0; i < nums.size(); i++){
            sum = sum + nums[i];
            max_sum = max(max_sum , sum);
            if(sum < 0)
                sum = 0;
        }
        return max_sum;
    }
};
```