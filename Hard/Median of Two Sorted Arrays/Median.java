import java.util.*;

class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] nums = new int[nums1.length + nums2.length];
        System.arraycopy(nums1, 0, nums, 0, nums1.length);
        System.arraycopy(nums2, 0, nums, nums1.length, nums2.length);
        Arrays.sort(nums);
        return (nums[nums.length >> 1] + nums[(nums.length - 1) >> 1]) / 2.0;
    }
}

class Median {
    public static void main(String[] args) {
        Solution obj = new Solution();
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
		int i;
        for (i = 0; i < t; i++) {
            int n = sc.nextInt();
			int m = sc.nextInt();
			int[] nums1 = new int[n];
			int[] nums2 = new int[m];
			for(i = 0; i < n; i++) {
				nums1[i] = sc.nextInt();
			}
			for(i = 0; i < m; i++) {
				nums2[i] = sc.nextInt();
			}
            System.out.println(obj.findMedianSortedArrays(nums1, nums2));
        }
        sc.close();
    }
}
