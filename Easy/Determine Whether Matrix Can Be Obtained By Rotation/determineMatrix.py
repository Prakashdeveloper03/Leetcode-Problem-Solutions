from typing import List

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if target == mat:
            return True
        for _ in range(3, 0, -1):
            n = len(mat)
            mat2 = []
            for j in range(n):
                temp = []
                i = n - 1
                while i >= 0:
                    temp.append(mat[i][j])
                    i -= 1
                mat2.append(temp)
            if mat2 == target:
                return True
            else:
                mat = mat2
        return False


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        mat = []
        target = []
        for _ in range(n):
            temp = list(map(int, input().split()))
            mat.append(temp)
        for _ in range(n):
            temp = list(map(int, input().split()))
            target.append(temp)
        print(Solution().findRotation(mat, target))
