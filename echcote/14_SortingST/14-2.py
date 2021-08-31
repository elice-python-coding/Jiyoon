'''
안테나
'''
import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

max_distance = max(array)
min_distance = 999999999
result = 0

for i in range(max_distance):
    tmp = 0
    for house in array:
        distance = abs(i-house)
        tmp += distance
    print(i, tmp)
    if tmp < min_distance:
        min_distance = tmp
        result = i

print(result)