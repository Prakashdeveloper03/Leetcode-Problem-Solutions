from typing import List
from heapq import heapify, nsmallest


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [
            (pow(points[i][0], 2) + pow(points[i][1], 2), i) for i in range(len(points))
        ]
        heapify(heap)
        return [points[x[1]] for x in nsmallest(k, heap)]


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        points = []
        for _ in range(n):
            temp = list(map(int, input().strip().split()))
            points.append(temp)
        k = int(input())
        print(Solution().kClosest(points, k))
