# Flatten Nested List Iterator
![made-with-Python](https://img.shields.io/badge/Made%20with-Python-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

You are given a nested list of integers `nestedList`. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an `iterator` to flatten it.

Implement the NestedIterator class:
- **NestedIterator(List<NestedInteger> nestedList)** Initializes the iterator with the nested list nestedList.
- **int next()** Returns the next integer in the nested list.
- **boolean hasNext()** Returns true if there are still some integers in the nested list and false otherwise.

Your code will be tested with the following pseudocode:
```py
# initialize iterator with nestedList
res = []
while iterator.hasNext()
    append iterator.next() to the end of res
return res
```
If `res` matches the expected flattened list, then your code will be judged as correct.


__Example 1:__
```
Input: nestedList = [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].
```
__Example 2:__
```
Input: nestedList = [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].
```

__Constraints:__
- 1 <= nestedList.length <= 500
- The values of the integers in the nested list is in the range [-10<sup>6</sup>, 10<sup>6</sup>].

### Solution
```py
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.flattedList = []
        for i in range(len(nestedList)):
            nestedArray = self.flat(nestedList[i])
            self.flattedList.extend(nestedArray)
        print(self.flattedList)
        self.currentIndex = 0

    def flat(self, nestedInteger: NestedInteger) -> list:
        array = []
        if nestedInteger.isInteger():
            array.append(nestedInteger.getInteger())
        else:
            nestedIntegerList = nestedInteger.getList()
            for nestedInteger in nestedIntegerList:
                tmpArray = self.flat(nestedInteger)
                array.extend(tmpArray)
        return array

    def next(self) -> int:
        if self.currentIndex > len(self.flattedList) - 1:
            return self.flattedList[self.currentIndex]
        result = self.flattedList[self.currentIndex]
        self.currentIndex += 1
        return result

    def hasNext(self) -> bool:
        return self.currentIndex <= len(self.flattedList) - 1
```