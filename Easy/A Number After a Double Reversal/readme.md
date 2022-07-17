# A Number After a Double Reversal
![made-with-Java](https://img.shields.io/badge/Made%20with-Java-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Reversing an integer means to reverse all its digits.
- For example, reversing 2021 gives 1202. Reversing 12300 gives 321 as the **leading zeros are not retained**.

Given an integer num, reverse num to get reversed1, then reverse reversed1 to get reversed2. **Return true** if reversed2 equals num. Otherwise **return false**.

__Example 1:__
```
Input: num = 526
Output: true
Explanation: Reverse num to get 625, then reverse 625 to get 526, which equals num.
```

__Example 2:__
```
Input: num = 1800
Output: false
Explanation: Reverse num to get 81, then reverse 81 to get 18, which does not equal num.
```

__Example 3:__
```
Input: num = 0
Output: true
Explanation: Reverse num to get 0, then reverse 0 to get 0, which equals num.
```

__Constraints:__
- 0 <= num <= 10<sup>6</sup>

### Solution
```java
import java.util.Scanner;

class Solution {
	public int reverse(int x) {
		int reversedNumber = 0;
		for (; x != 0; x /= 10) {
			reversedNumber = (reversedNumber * 10) + (x % 10);
		}
		if (reversedNumber > -2147483647 && reversedNumber < 2147483646) {
			return reversedNumber;
		}
		return 0;
	}

	public boolean isSameAfterReversals(int num) {
		int rev = reverse(reverse(num));
		if (rev == num) {
			return true;
		}
		return false;
	}
}

class doubleReversal {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Solution obj = new Solution();
		int t = sc.nextInt();
		for (int i = 0; i < t; i++) {
			int num = sc.nextInt();
			System.out.println(obj.isSameAfterReversals(num));
		}
		sc.close();
	}
}
```