'''01 유효한 팰린드롬'''
import re
import collections

# 내 풀이
def isPalindrome(word):
    word = word.strip().lower()
    new_word = [char for char in word if char.isalnum()]

    l = len(new_word)
    for i in range(l//2):
        if new_word[i] != new_word[l-i-1]:
            return False
    return True

# 리스트로 변환
def isPalindrome1(self, s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    # 팰린드롬 여부 판별
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
    return True

# 데크 자료형을 이용한 최적화
def isPalindrome2(self, s: str) -> bool:
    # 자료형 deque로 선언
    strs = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())        
    while len(strs) > 1:
        if strs.popleft != strs.pop():
            return False
    return True

# 슬라이싱 사용
def isPalindrome3(self, s: str) -> bool:
    s = s.lower()
    # 정규식으로 불필요한 문자 필터링
    s = re.sub('[^a-z0-9]', '', s)
    
    return s == s[::-1] # 슬라이싱