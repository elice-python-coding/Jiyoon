'''
실전문제 3번. 성적이 낮은 순서로 학생 출력하기
'''
n = int(input())

grade = []
for i in range(n):
    name, score = input().split()
    grade.append([name, int(score)])

grade = sorted(grade, key=lambda student:student[1])

for student in grade:
    print(student[0], end=' ')