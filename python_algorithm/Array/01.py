'''두 수의 합'''

# 내 풀이(비효율적)
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


# in을 이용한 탐색
def twoSum1(nums, target):
    # i는 index, n은 value
    for i, n in enumerate(nums):
        # n에 더해서 target이 되는 값
        complement = target - n

        # complement가 i번째 이후에 있는지 검사
        if complement in nums[i + 1:]:
            # complement의 index
            # i번째 이후의 리스트를 슬라이싱하고
            # complement의 index를 찾은 뒤 i+1을 더한다.
            return [nums.index(n), nums[i+1:].index(complement) + (i+1)]


# 첫 번째 수를 뺀 결과 키 조회
def twoSum2(nums, target):
    nums_map = {}
    # 키와 값을 바꿔서 딕셔너리로 저장
    for i, num in enumerate(nums):
        nums_map[num] = i

    # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map(target - num):
            return [i, nums_map[target - num]]


# 조회 구조 개선
def twoSum3(nums, target):
    nums_map = {}
    # 하나의 for문으로 통합
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i
    

