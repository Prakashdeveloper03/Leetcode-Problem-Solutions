# My Calendar I
![made-with-Python](https://img.shields.io/badge/Made%20with-Python-007396.svg)
![terminal](https://img.shields.io/badge/Windows%20Terminal-4D4D4D?logo=windows%20terminal&logoColor=white)
![sublime text](https://img.shields.io/badge/sublime_text-%23575757.svg?logo=sublime-text&logoColor=important)
![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?logo=visual%20studio%20code&logoColor=white)

You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

The event can be represented as a pair of integers `start` and `end` that represents a booking on the half-open interval [start, end], the range of real numbers x such that start <= x < end.

Implement the MyCalendar class:
- **MyCalendar()** Initializes the calendar object.
- **boolean book(int start, int end)** Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.


__Example 1:__
```
Input
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]
Output
[null, true, false, true]

Explanation
MyCalendar myCalendar = new MyCalendar();
myCalendar.book(10, 20); // return True
myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.
```

__Constraints:__
- 0 <= start < end <= 10<sup>9</sup>
- At most 1000 calls will be made to book.


### Solution
```py
from cmath import inf
from bisect import bisect_right, insort

class MyCalendar:
    def __init__(self):
        self.start, self.end = [float(-inf)], [float(-inf)]

    def book(self, start: int, end: int) -> bool:
        s = self.start
        e = self.end
        closes_end = bisect_right(e, start)
        if closes_end == len(e):
            s.append(start)
            e.append(end)
            return True
        if e[closes_end - 1] <= start and s[closes_end] >= end:
            insort(s, start, closes_end)
            insort(e, end, closes_end)
            return True
        return False
```