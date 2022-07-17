# Reverse Integer
![made-with-Java](https://img.shields.io/badge/Made%20with-Java-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2<sup>31</sup>, 2<sup>31</sup> - 1], then return 0.

**Assume the environment does not allow you to store 64-bit integers (signed or unsigned).**

__Example 1:__
```
Input: x = 123
Output: 321
```

__Example 2:__
```
Input: x = -123
Output: -321
```

__Example 3:__
```
Input: x = 120
Output: 21
```

__Constraints:__
- -2<sup>31</sup> <= x <= 2<sup>31</sup> - 1

### Solution
```java
import java.util.Scanner;

class Solution {
	public int reverse(int x) {
		int sign = x < 0 ? -1 : 1;
		long result = 0;
		x = Math.abs(x);
		while (x != 0) {
			result = (result * 10) + (x % 10);
			x = x / 10;
			if (result < Integer.MIN_VALUE || result > Integer.MAX_VALUE) {
				return 0;
			}
		}
		if (sign == -1)
			return -1 * (int) result;
		else
			return (int) result;
	}
}

class reverseInt {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Solution obj = new Solution();
		int t = sc.nextInt();
		for (int i = 0; i < t; i++) {
			int num = sc.nextInt();
			System.out.println(obj.reverse(num));
		}
		sc.close();
	}
}
```