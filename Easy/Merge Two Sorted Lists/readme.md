# Merge Two Sorted Lists
![made-with-Java](https://img.shields.io/badge/Made%20with-Java-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the **head of the merged linked list**.

__Example 1:__
```
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```
__Example 2:__
```
Input: list1 = [], list2 = []
Output: []
```
__Example 3:__
```
Input: list1 = [], list2 = [0]
Output: [0]
```

__Constraints:__
- The number of nodes in both lists is in the range [0, 50].
- 100 <= Node.val <= 100
- Both list1 and list2 are sorted in **non-decreasing** order.

### Solution
```java
class ListNode {
	int val;
	ListNode next;

	ListNode() {
	}

	ListNode(int val) {
		this.val = val;
	}

	ListNode(int val, ListNode next) {
		this.val = val;
		this.next = next;
	}
}

class Solution {
	public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
		ListNode temp = new ListNode();
		ListNode tail = temp;

		while (list1 != null && list2 != null) {
			if (list1.val < list2.val) {
				tail.next = list1;
				list1 = list1.next;
				tail = tail.next;
			} else {
				tail.next = list2;
				list2 = list2.next;
				tail = tail.next;
			}
		}
		while (list1 != null) {
			tail.next = list1;
			list1 = list1.next;
			tail = tail.next;
		}
		while (list2 != null) {
			tail.next = list2;
			list2 = list2.next;
			tail = tail.next;
		}
		return temp.next;
	}
}
```

