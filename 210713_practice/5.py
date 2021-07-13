# 카카오톡 튜플

from collections import Counter

def solution(s):
    _list = s.replace('{', '').replace('}', '').split(',')
    tmp = Counter(_list).most_common()
    
    return [int(num) for num, _ in tmp]