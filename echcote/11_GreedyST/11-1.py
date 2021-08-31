n = int(input())
data = list(map(int, input().split()))

result = 0
data.sort()

while len(data) > 0:
    maximum = max(data)

    # data의 길이가 max보다 크면 뒤에서부터 max 갯수만큼 삭제
    if len(data) >= maximum:
        data = data[:-maximum]
        result += 1
    else:
        break

print(result)
    