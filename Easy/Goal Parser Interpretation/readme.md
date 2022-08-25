# Goal Parser Interpretation
![made-with-Python](https://img.shields.io/badge/Made%20with-Python-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

You own a **Goal Parser** that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

Given the string `command`, return the Goal Parser's interpretation of `command`.

__Example 1:__
```
Input: command = "G()(al)"
Output: "Goal"
Explanation: The Goal Parser interprets the command as follows:
G -> G
() -> o
(al) -> al
The final concatenated result is "Goal".
```
__Example 2:__
```
Input: command = "G()()()()(al)"
Output: "Gooooal"
```

__Example 3:__
```
Input: command = "(al)G(al)()()G"
Output: "alGalooG"
```

__Constraints:__
- 1 <= command.length <= 100
- command consists of "G", "()", and/or "(al)" in some order.

### Solution
```py
class Solution:
    def interpret(self, command: str) -> str:
        return command.replace("()", "o").replace("(al)", "al")

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        command = input()
        print(Solution().interpret(command))
```