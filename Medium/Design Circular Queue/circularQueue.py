class MyCircularQueue(object):
    def __init__(self, k):
        self.queue = []
        self.k = k

    def enQueue(self, value):
        if len(self.queue) < self.k:
            self.queue.append(value)
            return True
        return False

    def deQueue(self):
        if len(self.queue) > 0:
            self.queue.pop(0)
            return True
        return False

    def Front(self):
        return self.queue[0] if len(self.queue) > 0 else -1

    def Rear(self):
        return self.queue[-1] if len(self.queue) > 0 else -1

    def isEmpty(self):
        return self.queue == []

    def isFull(self):
        return len(self.queue) == self.k
