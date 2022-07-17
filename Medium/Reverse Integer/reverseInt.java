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