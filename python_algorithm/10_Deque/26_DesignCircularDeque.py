'''원형 데크 디자인'''

class ListNode:
    prev = None
    next = None
    def __init__(self, k):
        self.value = k


class MyCircularDeque:
    front = None
    rear = None
    len = 0
    def __init__(self, k: int):
        self.size = k

    def insertFront(self, value: int) -> bool:
        node = ListNode(value)
        if self.front is None:
            self.front = node
            self.rear = node
        elif self.len == 1:
            tmp = self.front
            self.front.prev = node
            self.rear.prev = node
            self.front = node
            self.front.next = tmp
        elif self.len < self.size:
            tmp = self.front
            self.front.prev = node
            self.front = node
            self.front.next = tmp
        else:
            return False
        self.len += 1
        return True

    def insertLast(self, value: int) -> bool:
        node = ListNode(value)
        if self.rear is None:
            self.front = node
            self.rear = node
        elif self.len == 1:
            tmp = self.rear
            self.front.next = node
            self.rear.next = node
            self.rear = node
            self.rear.prev = tmp
        elif self.len < self.size:
            tmp = self.rear
            self.rear.next = node
            self.rear = node
            self.rear.prev = tmp
        else:
            return False
        self.len += 1
        return True

    def deleteFront(self) -> bool:
        if self.len == 1:
            self.front = None
            self.rear = None
            self.len = 0
            return True
        elif self.front is not None:
            tmp = self.front.next
            self.front = tmp
            self.front.prev = None
            self.len -= 1
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        if self.len == 1:
            self.front = None
            self.rear = None
            self.len = 0
            return True
        elif self.rear is not None:
            tmp = self.rear.prev
            self.rear = tmp
            self.rear.next = None
            self.len -= 1
            return True
        else:
            return False

    def getFront(self) -> int:
        if self.front:
            return self.front.value
        return -1

    def getRear(self) -> int:
        if self.rear:
            return self.rear.value
        return -1

    def isEmpty(self) -> bool:
        if self.len == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.len >= self.size:
            return True
        return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()