# Median of Two Sorted Arrays
![made-with-Java](https://img.shields.io/badge/Made%20with-Java-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the **median of the two sorted arrays**.

The overall run time complexity should be **O(log (m+n))**.

__Example 1:__
```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
```
__Example 2:__
```
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
```

__Constraints:__
- nums1.length == m
- nums2.length == n
- 0 <= m <= 1000
- 0 <= n <= 1000
- 1 <= m + n <= 2000
- -10<sup>6</sup> <= nums1[i], nums2[i] <= 10<sup>6</sup>


### Solution
```java
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
```

