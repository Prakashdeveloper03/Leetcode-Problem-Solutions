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
