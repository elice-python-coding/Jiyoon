class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    '''
    연결 리스트를 이용하여 다음의 method들을 작성하세요.
    '''
    def __init__(self) :
        '''
        큐 myQueue을 만듭니다.
        '''
        self.head = None
        self.tail = None
        self.size_ = 0

    def push(self, n) :
        '''
        queue에 정수 n을 넣습니다.
        '''
        node = Node(n)
        if self.empty() == 1:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.size_ += 1

    def pop(self) :
        '''
        queue에서 가장 앞에 있는 정수를 제거합니다. 만약 queue에 들어있는 값이 없을 경우에는 아무 일도 하지 않습니다. 
        '''
        if self.size_ < 1:
            return
            
        else:
            self.head = self.head.next
            self.size_ -= 1
            

    def size(self) :
        '''
        queue에 들어 있는 정수의 개수를 return 합니다.
        '''
        return self.size_

    def empty(self) :
        '''
        queue이 비어있다면 1, 아니면 0을 return 합니다.
        '''
        if self.size_ == 0:
            return 1
        else:
            return 0

    def front(self) :
        '''
        queue의 가장 앞에 있는 정수를 return 합니다. 만약 queue에 들어있는 값이 없을 경우에는 -1을 return 합니다.
        '''
        if self.size_ < 1:
            return -1
        else:
            return self.head.data

    def back(self) :
        '''
        queue의 가장 뒤에 있는 정수를 return 합니다. 만약 queue에 들어있는 값이 없을 경우에는 -1을 return 합니다.
        '''
        if self.size_ < 1:
            return -1
        else:
            return self.tail.data