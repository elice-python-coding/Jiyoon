# 1920

# N개의 정수 A[1], A[2], ..., A[N]이 주어져 있을 때, 이 안에 x라는 정수가 존재하는지 알아내라
# 제약 조건 new_id의 길이는 ?

#input 느리다...
import sys
input = sys.stdin.readline #함수의 대입

N = int(input())
_set = set(map(int, input().split()))

M = int(input())

''' 보통은 이렇게 짠다~

_list = [list(map(int, input.split()))]
for dt in _list:
    if dt in _set:
        print(1)
    else:
        print(0)
'''

print(*[1 if dt in _set else 0 for dt in map(int, input.split())], sep="\n")

# 위 코드가 너무 길면 이렇게 해도 ok
_list = [list(map(int, input.split()))]
print(*[1 if dt in _set else 0 for dt in _list], sep="\n")
