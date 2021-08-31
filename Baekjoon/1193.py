'''https://www.acmicpc.net/problem/1193'''

n = int(input())

total = 0
i = 1
while n > total:
    total += i
    i += 1

tmp  = n - (total - i + 1)
if i % 2 == 0:
    print(f"{i-tmp}/{tmp}")
else:
    print(f"{tmp}/{i-tmp}")