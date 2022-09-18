# Insert Delete GetRandom O(1)
![made-with-Python](https://img.shields.io/badge/Made%20with-Python-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Implement the RandomizedSet class:
- **RandomizedSet()** Initializes the RandomizedSet object.
- **bool insert(int val)** Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
- **bool remove(int val)** Removes an item val from the set if present. Returns true if the item was present, false otherwise.
- **int getRandom()** Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.

You must implement the functions of the class such that each function works in average O(1) time complexity.

__Example 1:__
```
Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
```

__Constraints:__
- -2<sup>31</sup> <= val <= 2<sup>31</sup> - 1
- At most 2 * 10<sup>5</sup> calls will be made to insert, remove, and getRandom.
- There will be at least one element in the data structure when getRandom is called.

### Solution
```py
from random import choice

class RandomizedSet:
    def __init__(self):
        self.dict = {}
        self.list = []

    def insert(self, val):
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val):
        if val in self.dict:
            last_element_val, last_element_idx = self.list[-1], self.dict[val]
            self.list[last_element_idx], self.dict[last_element_val] = (
                last_element_val,
                last_element_idx,
            )
            self.list.pop()
            del self.dict[val]
            return True
        return False

    def getRandom(self):
        return choice(self.list)
```