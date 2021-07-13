# 카카오톡 튜플
# https://programmers.co.kr/learn/courses/30/lessons/64065

from collections import Counter

def solution(s):
    _list = s.replace('{', '').replace('}', '').split(',')
    tmp = Counter(_list).most_common()
    
    return [int(num) for num, _ in tmp]   # _는 의미 없는?