'''배열 파티션 1'''

# 내 풀이
def arrayPartition(nums):
    nums.sort()
    return sum([nums[i] for i in range(len(nums)) if i % 2 == 0])


# 오름차순 풀이
def arrayPartition1(nums):
    nums.sort()
    pair = []
    sum = 0

    for n in nums:
        # 앞에서부터 오름차순으로 페어를 만들어서 합 계산
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []

    return sum


# 파이썬다운 방식
def arrayPartition2(nums):
    return sum(sorted(nums)[::2])

print(arrayPartition([1, 4, 3, 2])) 