'''https://www.acmicpc.net/problem/2292'''

n = int(input())

i = 1
total = 1

while n > total:
    total += i * 6
    i += 1

print(i)