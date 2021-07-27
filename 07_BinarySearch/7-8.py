'''
실전 3번. 떡볶이 떡 만들기
'''
def binary_search(dduck, target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2
    array = [x - mid if x > mid else 0 for x in dduck]
    total = sum(array) 
    print(array, total)

    if total > target:
        return binary_search(dduck, target, mid + 1, end)
    elif total < target:
        return binary_search(dduck, target, start, mid - 1)
    else:
        return mid



n, m = map(int, input().split())
dduck = list(map(int, input().split()))
max_dduck = max(dduck)

print(binary_search(dduck, m, 0, max_dduck))