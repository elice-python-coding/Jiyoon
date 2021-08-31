'''
[실전문제 5번] 효율적인 화폐 구성
N가지 종류의 화폐가 있다. 개수를 최소한으로 이용해 합이 M원이 되도록 하려고 한다. 각 화폐는 몇 개라도 사용할 수 있고, 순서는 고려하지 않는다.
'''


n, m = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))

d = [10001] * (m + 1)

d[0] = 0
for i in range(n):
    for j in range(coins[i], m+1):
        d[j] = min(d[j], d[j-coins[i]]+1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])