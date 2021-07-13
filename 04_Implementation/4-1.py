N = int(input())
direction = list(map(str, input().split()))

result = [1,1]

for dir in direction:
    if dir == 'L' and result[1] > 1:
        result[1] -= 1
    elif dir == 'R' and result[1] < N:
        result[1] += 1
    elif dir == 'U' and result[0] > 1:
        result[0] -= 1
    elif dir == 'D' and result[0] < N:
        result[0] += 1

print(result)
