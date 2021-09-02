'''https://www.acmicpc.net/problem/1235'''

n = int(input())
students = [int(input().strip()) for _ in range(n)]

k = 1
while True:
    list_k = []
    for student in students:
        list_k.append(str(student)[-k:])
    
    if len(set(list_k)) == len(students):
        break
    k += 1

print(k)