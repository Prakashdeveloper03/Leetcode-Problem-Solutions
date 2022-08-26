from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_index = {key: index for index, key in enumerate(order)}
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            for j in range(len(word1)):
                if j == len(word2):
                    return False
                if word1[j] != word2[j]:
                    if order_index.get(word2[j]) < order_index.get(word1[j]):
                        return False
                    break
        return True


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        words = list(input().split())
        order = input()
        print(Solution().isAlienSorted(words, order))
