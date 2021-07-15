'''
Deque 클래스를 구현하세요.
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class Deque:
    '''
    아래의 method들을 작성하세요.
    '''
    def __init__(self) :
        '''
        문제의 조건대로 값들을 담을 수 있게끔 
        Deque 클래스의 생성자를 자유롭게 정의하세요.
        '''
        self.first = None
        self.rear = None
        self.my_size = 0

        pass

    def push_front(self, n) :
        '''
        덱에 정수 n을 맨 앞에 넣습니다.
        '''
        node = Node(n)
        
        if self.my_size == 0:
            self.first = node
            self.rear = node
        elif self.my_size == 1:
            self.first = node
            self.first.next = self.rear
            self.rear.prev = self.first
        else:
            self.first.prev = node
            temp = self.first
            self.first = node
            self.first.next = temp
        self.my_size += 1
    
    def push_back(self, n) :
        '''
        덱에 정수 n을 맨 뒤에 넣습니다.
        '''
        node = Node(n)
        
        if self.my_size == 0:
            self.first = node
            self.rear = node
        elif self.my_size == 1:
            self.first.next = node
            self.rear = node
            self.rear.prev = self.first
        else:
            self.rear.next = node
            temp = self.rear
            self.rear = node
            self.rear.prev = temp
        self.my_size += 1
    

    def pop_front(self) :
        '''
        덱에서 가장 앞에 있는 정수를 제거합니다. 만약 덱에 들어있는 값이 없을 경우에는 아무 일도 하지 않습니다. 
        '''
        if self.my_size == 0:
            return
        elif self.my_size == 1:
            self.first = None
            self.rear = None
        else:
            self.first = self.first.next
        self.my_size -= 1

    def pop_back(self) :
        '''
        덱에서 가장 뒤에 있는 정수를 제거합니다. 만약 덱에 들어있는 값이 없을 경우에는 아무 일도 하지 않습니다. 
        '''
        if self.my_size == 0:
            return
        elif self.my_size == 1:
            self.first = None
            self.rear = None
        else:
            self.rear = self.rear.prev
        self.my_size -= 1

    def size(self) :
        '''
        덱에 들어 있는 정수의 개수를 return 합니다.
        '''
        return self.my_size

    def empty(self) :
        '''
        덱이 비어있다면 1, 아니면 0을 return 합니다.
        '''
        if self.my_size == 0:
            return 1
        else:
            return 0
            
    def front(self) :
        '''
        덱의 가장 앞에 있는 정수를 return 합니다. 만약 덱에 들어있는 값이 없을 경우에는 -1을 return 합니다.
        '''
        if self.my_size == 0:
            return -1
        else:
            return self.first.data

    def back(self) :
        '''
        덱의 가장 뒤에 있는 정수를 return 합니다. 만약 덱에 들어있는 값이 없을 경우에는 -1을 return 합니다.
        '''
        if self.my_size == 0:
            return -1
        else:
            return self.rear.data
        