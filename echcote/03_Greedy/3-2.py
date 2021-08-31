text = input().split(" ")
N = int(text[0])
M = int(text[1])
K = int(text[2])

nums = input().split(" ")

for i in range(N):
    nums[i] = int(nums[i])

nums.sort()

result = 0
count = 0

for j in range(M):
    if count < K:
        result += nums[-1]
        count += 1
    else:
        count = 0
        result += nums[-2]

print(result)