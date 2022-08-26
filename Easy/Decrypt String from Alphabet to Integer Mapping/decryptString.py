import string


class Solution:
    def freqAlphabets(self, s: str) -> str:
        result = []
        i = 0
        alphabets = string.ascii_lowercase
        while i < len(s):
            if (i + 1 < len(s) and s[i + 1] == "#") or s[i] == "#":
                i += 1
                continue
            elif i + 2 < len(s) and s[i + 2] == "#":
                result.append(alphabets[int(s[i : i + 2]) - 1])
            else:
                result.append(alphabets[int(s[i]) - 1])
            i += 1
        return "".join(result)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        print(Solution().freqAlphabets(s))
