from heapq import heappush, heappop, heapify


class SeatManager:
    def __init__(self, n: int):
        self.minheap = list(range(1, n + 1))
        heapify(self.minheap)

    def reserve(self) -> int:
        return heappop(self.minheap)

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.minheap, seatNumber)
