class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        digit_map = {
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "0": 0,
        }
        convert = lambda num: sum(
            digit_map[num[i - 1]] * 10 ** (len(num) - i) for i in range(len(num), 0, -1)
        )
        return str(convert(num1) * convert(num2))


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        num1, num2 = input().split()
        print(Solution().multiply(num1, num2))
