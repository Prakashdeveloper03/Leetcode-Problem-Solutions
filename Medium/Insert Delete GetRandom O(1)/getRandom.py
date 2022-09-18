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
