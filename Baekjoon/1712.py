'''https://www.acmicpc.net/problem/1712'''

a, b, c = map(int, input().split())

# 한 대 팔았을 때 이익
profit = c - b

if profit <= 0:
    print(-1)
else:
    n = a // (c - b) + 1
    print(n)