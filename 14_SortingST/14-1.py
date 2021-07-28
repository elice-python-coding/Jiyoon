'''
국영수
'''
import sys
input = sys.stdin.readline

n = int(input())
array = []

for i in range(n):
    data = list(map(str, input().split()))
    array.append([data[0], int(data[1]), int(data[2]), int(data[3])])

array.sort(key = lambda x:(-x[1], x[2], -x[3], x[0]))

for student in array:
    print(student[0]) 