'''
5-1.py 스택 예제 ------------------------------------------------------
'''

stack = []

# 삽입(5) - 삽입(2) - 삽입(3) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)         # [5, 2, 1]
print(stack[::-1])   # [1, 2, 5]


'''
5-2.py 큐 예제 --------------------------------------------------------
'''
from collections import deque

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.pop()
queue.append(1)
queue.append(4)
queue.pop()

print(queue)    # [5, 2, 1]
queue.reverse()
print(queue)    # [1, 2, 5]