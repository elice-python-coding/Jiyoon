COINS = [500, 100, 50, 10]

n = int(input())

count = 0

for i in range(len(COINS)):
    count += n // COINS[i]
    n %= COINS[i]

print(count)