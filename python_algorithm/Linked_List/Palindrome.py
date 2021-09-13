'''13. 팰린드롬 연결 리스트'''

from collections import deque

# 내 풀이(1184ms)
def Palindrome(head):
    l = deque()
    while head is not None:
        l.append(head.val)
        head = head.next    
    while len(l) > 1:
        if l.popleft() != l.pop():
            return False
    return True

# (내 풀이랑 비슷해서 pass)
# 리스트 변환
# 데크를 이용한 최적화


# 런너를 이용한 우아한 풀이
def isPalindrome(head):
    rev = None
    slow = fast = head
    # 런너를 이용해 역순 연결 리스트 구성
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next
    
    # 팰린드롬 여부 확인
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    return not rev