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