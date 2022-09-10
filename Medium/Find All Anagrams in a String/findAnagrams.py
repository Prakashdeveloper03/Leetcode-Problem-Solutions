from collections import deque, Counter, defaultdict
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        stat_p = Counter(p)
        stat_s = defaultdict(int)
        ind, queue = 0, deque([])
        ans = []
        while ind != len(s):
            if s[ind] not in stat_p:
                while queue:
                    pop = queue.popleft()
                    stat_s[pop[0]] -= 1
            else:
                queue.append((s[ind], ind))
                stat_s[s[ind]] += 1
            if len(queue) == len(p):
                pop = queue.popleft()
                if not set(stat_p.items()) ^ set(stat_s.items()):
                    ans.append(pop[1])
                stat_s[pop[0]] -= 1
            ind += 1
        return ans


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s, p = input().strip().split()
        print(Solution().findAnagrams(s, p))
