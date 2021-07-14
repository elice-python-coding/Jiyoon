nums = list(input())

# 입력받은 nums를 int형으로 변환하고 정렬
nums = [int(num) for num in nums]
nums.sort()
result = 0

for num in nums:
    # result가 0 이거나 num 이 0 또는 1 이면 result에 더해준다.
    if num == 0 or num == 1 or result == 0:
        result += num
    else:
        result *= num

print(result)


