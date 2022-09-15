# Seat Reservation Manager
![made-with-Python](https://img.shields.io/badge/Made%20with-Python-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

Design a system that manages the reservation state of `n` seats that are numbered from 1 to n.

Implement the `SeatManager` class:
- **SeatManager(int n)** Initializes a SeatManager object that will manage n seats numbered from 1 to n. All seats are initially available.
- **int reserve()** Fetches the smallest-numbered unreserved seat, reserves it, and returns its number.
- **void unreserve(int seatNumber)** Unreserves the seat with the given seatNumber.

__Example 1:__
```
Input
["SeatManager", "reserve", "reserve", "unreserve", "reserve", "reserve", "reserve", "reserve", "unreserve"]
[[5], [], [], [2], [], [], [], [], [5]]
Output
[null, 1, 2, null, 2, 3, 4, 5, null]

Explanation
SeatManager seatManager = new SeatManager(5); // Initializes a SeatManager with 5 seats.
seatManager.reserve();    // All seats are available, so return the lowest numbered seat, which is 1.
seatManager.reserve();    // The available seats are [2,3,4,5], so return the lowest of them, which is 2.
seatManager.unreserve(2); // Unreserve seat 2, so now the available seats are [2,3,4,5].
seatManager.reserve();    // The available seats are [2,3,4,5], so return the lowest of them, which is 2.
seatManager.reserve();    // The available seats are [3,4,5], so return the lowest of them, which is 3.
seatManager.reserve();    // The available seats are [4,5], so return the lowest of them, which is 4.
seatManager.reserve();    // The only available seat is seat 5, so return 5.
seatManager.unreserve(5); // Unreserve seat 5, so now the available seats are [5].
```

__Constraints:__
- 1 <= n <= 10<sup>5</sup>
- 1 <= seatNumber <= n
- For each call to reserve, it is guaranteed that there will be at least one unreserved seat.
- For each call to unreserve, it is guaranteed that seatNumber will be reserved.
- At most 10<sup>5</sup> calls in total will be made to reserve and unreserve.

### Solution
```py
from heapq import heappush, heappop, heapify

class SeatManager:
    def __init__(self, n: int):
        self.minheap = list(range(1, n + 1))
        heapify(self.minheap)

    def reserve(self) -> int:
        return heappop(self.minheap)

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.minheap, seatNumber)
```