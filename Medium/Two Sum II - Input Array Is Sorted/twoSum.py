from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(numbers):
            if target - num in dic:
                return [dic[target - num] + 1, i + 1]
            dic[num] = i


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        numbers = list(map(int, input().strip().split()))
        target = int(input())
        print(Solution().twoSum(numbers, target))
