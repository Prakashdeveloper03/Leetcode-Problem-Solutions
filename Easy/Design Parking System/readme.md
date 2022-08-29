# Design Parking System
![made-with-Python](https://img.shields.io/badge/Made%20with-Python-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Design a parking system for a parking lot. The parking lot has three kinds of parking spaces: big, medium, and small, with a fixed number of slots for each size.

Implement the `ParkingSystem` class:
- **ParkingSystem(int big, int medium, int small)** Initializes object of the ParkingSystem class. The number of slots for each parking space are given as part of the constructor.
- **bool addCar(int carType)** Checks whether there is a parking space of carType for the car that wants to get into the parking lot. `carType` can be of three kinds: big, medium, or small, which are represented by 1, 2, and 3 respectively. **A car can only park in a parking space of its** carType. If there is no space available, return false, else park the car in that size space and return true.

__Example 1:__
```
Input
["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
[[1, 1, 0], [1], [2], [3], [1]]
Output
[null, true, true, false, false]

Explanation
ParkingSystem parkingSystem = new ParkingSystem(1, 1, 0);
parkingSystem.addCar(1); // return true because there is 1 available slot for a big car
parkingSystem.addCar(2); // return true because there is 1 available slot for a medium car
parkingSystem.addCar(3); // return false because there is no available slot for a small car
parkingSystem.addCar(1); // return false because there is no available slot for a big car. It is already occupied.
```

__Constraints:__
- 0 <= big, medium, small <= 1000
- carType is 1, 2, or 3
- At most 1000 calls will be made to addCar
  
### Solution
```py
class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.capacity = {1: big, 2: medium, 3: small}

    def addCar(self, carType: int) -> bool:
        if self.capacity[carType] > 0:
            self.capacity[carType] = self.capacity[carType] - 1
            return True
        return False

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        big, medium, small = tuple(map(int, input().split()))
        obj = ParkingSystem(big, medium, small)
        n = int(input())
        for _ in range(n):
            carType = int(input())
            print(obj.addCar(carType))
```