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
