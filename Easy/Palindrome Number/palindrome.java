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