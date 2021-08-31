N, M, K = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

first = nums[-1] # 가장 큰 수
second = nums[-2] #두 번째로 큰 수

count = M//(K+1)*K + M%(K+2)

result = 0 # 결과
result += count * first
result += (M - count) * second

print(result)