from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = len(temperatures) * [0]
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                result[index] = i - index
            stack.append(i)
        return result


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        temperatures = list(map(int, input().split()))
        print(Solution().dailyTemperatures(temperatures))
