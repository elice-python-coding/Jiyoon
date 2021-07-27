'''
재귀 함수로 구현한 이진 탐색 소스코드
'''

def binary_search(array, target, start, end):
    if start > end:
        return "x"
    
    mid = (start + end) // 2

    if array[mid] > target:
        return binary_search(array, target, start, mid-1)
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)
    else:
        return mid + 1



# 원소의 개수(n)와 찾고자 하는 문자열(target) 입력받기
n, target = map(int, input().split())
# 전체 원소 입력받기
array = list(map(int, input().split()))

print(binary_search(array, target, 0, n-1))