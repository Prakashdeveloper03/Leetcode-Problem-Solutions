# Fizz Buzz
![made-with-Java](https://img.shields.io/badge/Made%20with-Java-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Given an integer n, return a string array answer (***1-indexed***) where:
- `answer[i] == "FizzBuzz"` if i is divisible by 3 and 5.
- `answer[i] == "Fizz"` if i is divisible by 3.
- `answer[i] == "Buzz"` if i is divisible by 5.
- `answer[i] == i (as a string)` if none of the above conditions are true.

__Example 1:__
```
Input: n = 3
Output: ["1","2","Fizz"]
```
__Example 2:__
```
Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
```
__Example 3:__
```
Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
```

__Constraints:__
- 1 <= n <= 10<sup>4</sup>

### Solution
```java
import java.util.*;

class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> result = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            if (i % 3 == 0 && i % 5 == 0) {
                result.add("FizzBuzz");
            } else if (i % 3 == 0) {
                result.add("Fizz");
            } else if (i % 5 == 0) {
                result.add("Buzz");
            } else {
                result.add(String.valueOf(i));
            }
        }
        return result;
    }
}

class FizzBuzz {
    public static void main(String[] args) {
        List<String> result = new ArrayList<>();
        Solution obj = new Solution();
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for (int i = 0; i < t; i++) {
            int n = sc.nextInt();
            result = obj.fizzBuzz(n);
            for (String s : result) {
                System.out.print(s + " ");
            }
        }
        sc.close();
    }
}
```

