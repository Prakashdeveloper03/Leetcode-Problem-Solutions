from itertools import zip_longest


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        alternated_words = list(zip_longest(word1, word2, fillvalue=""))
        merged_pairs = [x[0] + x[1] for x in alternated_words]
        return "".join(merged_pairs)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        word1 = input()
        word2 = input()
        print(Solution().mergeAlternately(word1, word2))
