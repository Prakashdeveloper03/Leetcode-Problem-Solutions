# Palindrome Number
![made-with-java](https://img.shields.io/badge/Made%20with-Java-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Given an integer `x`, return true if `x` is palindrome integer.

An integer is a **palindrome** when it reads the same backward as forward.

For example, `121` is a palindrome while `123` is not.

__Example 1:__
```
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
```
__Example 2:__
```
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
```
__Example 3:__
```
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
```

__Constraints:__
- -2<sup>31</sup> <= x <= 2<sup>31</sup> - 1

### Solution
```java
import java.util.Scanner;

class Solution {
	public boolean isPalindrome(int x) {
		int reversedNum = 0, temp = x;
		while (temp > 0) {
			reversedNum = reversedNum * 10 + temp % 10;
			temp = temp / 10;
		}
		return x == reversedNum;
	}
}

class palidrome {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Solution obj = new Solution();
		int t = sc.nextInt();
		for (int i = 0; i < t; i++) {
			int num = sc.nextInt();
			System.out.println(obj.isPalindrome(num));
		}
		sc.close();
	}
}
```

