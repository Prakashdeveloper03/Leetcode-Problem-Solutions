# First Unique Character in a String
![made-with-cpp](https://img.shields.io/badge/Made%20with-C++-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Given a string `s`, find the first non-repeating character in it and return its index. If it does not exist, return `-1`.

__Example 1:__
```
Input: s = "leetcode"
Output: 0
```

__Example 2:__
```
Input: s = "loveleetcode"
Output: 2
```

__Example 3:__
```
Input: s = "aabb"
Output: -1
```

__Constraints:__
- 1 <= s.length <= 10<sup>5</sup>
- `s` consists of only lowercase English letters.


### Solution
```cpp
class Solution
{
public:
    int firstUniqChar(string s)
    {
        map<char, int> hmap;
        for (int idx{}; idx < s.size(); idx++)
            hmap[s[idx]]++;

        for (int idx{}; idx < s.size(); idx++)
        {
            if (hmap[s[idx]] == 1)
                return idx;
        }
        return -1;
    }
};
```