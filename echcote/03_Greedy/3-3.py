N, M = map(int, input().split())
data = []

for i in range(N):
    data.append(list(map(int, input().split())))

result_min = 0

for i in range(N):
    data_min = min(data[i])
    if data_min > result_min:
        result_min = data_min
    
print(result_min)