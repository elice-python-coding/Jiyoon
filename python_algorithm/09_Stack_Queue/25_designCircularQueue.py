'''25. 원형 큐 디자인'''

class MyCircularQueue:

    def __init__(self, k: int):
        self.q = []
        self.len = k

    def enQueue(self, value: int) -> bool:
        if len(self.q) < self.len:
            self.q.append(value)
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if len(self.q) > 0:
            self.q.pop(0)
            return True
        else:
            return False

    def Front(self) -> int:
        if len(self.q) > 0:
            return self.q[0]
        else:
            return -1

    def Rear(self) -> int:
        if len(self.q) > 0:
            return self.q[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        return len(self.q) == 0

    def isFull(self) -> bool:
        return len(self.q) == self.len