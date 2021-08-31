'''
실전 문제 2번. 부품 찾기
'''

def binary_search(array, target, start, end):
    if start > end:
        return "no"
    
    mid = (start + end) // 2

    if array[mid] > target:
        return binary_search(array, target, start, mid-1)
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)
    else:
        return "yes"


# 가게 부품 입력받기
n = int(input())
array = list(map(int, input().split()))
array.sort()

# 손님 주문 입력받기
m = int(input())
order = list(map(int, input().split()))

for item in order:
    print(binary_search(array, item, 0, n), end=" ")
