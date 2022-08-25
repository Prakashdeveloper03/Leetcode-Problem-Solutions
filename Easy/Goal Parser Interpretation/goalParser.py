class Solution:
    def interpret(self, command: str) -> str:
        return command.replace("()", "o").replace("(al)", "al")


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        command = input()
        print(Solution().interpret(command))
