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