# Add Two Integers
![made-with-Java](https://img.shields.io/badge/Made%20with-Java-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Given two integers `num1` and `num2`, return the **sum** of the two integers.

__Example 1:__
```
Input: num1 = 12, num2 = 5
Output: 17
Explanation: num1 is 12, num2 is 5, and their sum is 12 + 5 = 17, so 17 is returned.
```
__Example 2:__
```
Input: num1 = -10, num2 = 4
Output: -6
Explanation: num1 + num2 = -6, so -6 is returned.
```

__Constraints:__
- -100 <= num1, num2 <= 100

### Solution
```java
import java.util.*;

class Solution {
	public int sum(int num1, int num2) {
		return num1 + num2;
	}
}

class AddIntegers {
	public static void main(String[] args) {
		Solution obj = new Solution();
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		for (int i = 0; i < t; i++) {
			int num1 = sc.nextInt();
			int num2 = sc.nextInt();
			System.out.println(obj.sum(num1, num2));
		}
		sc.close();
	}
}
```