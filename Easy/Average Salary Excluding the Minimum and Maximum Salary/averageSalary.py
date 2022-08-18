from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        salary.remove(min(salary))
        salary.remove(max(salary))
        return sum(salary) / len(salary)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        salary = list(map(int, input().strip().split()))
        print(Solution().average(salary))
