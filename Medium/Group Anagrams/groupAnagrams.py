from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for element in strs:
            if "".join(sorted(element)) not in group:
                group["".join(sorted(element))] = [element]
            else:
                group["".join(sorted(element))].extend([element])
        return list(group.values())


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        strs = list(input().strip().split())
        print(Solution().groupAnagrams(strs))
