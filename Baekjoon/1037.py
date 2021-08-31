'''https://www.acmicpc.net/problem/1037'''

n = int(input())
factors = list(map(int, input().split()))
factors.sort()
print(factors[0] * factors[-1])