'''8-1. Fibinacci Function(recursion)'''
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)

print(f'[recursion] fibo(10): {fibo(10)}')


'''8-2. Fibinacci Function(Memoization)'''
# 한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화
d = [0] *100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적이 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(f'[Memoization] fibo(99): {fibo(99)}')


'''8-3. Fibonacci(Top-down)'''
d = [0] *100

def fibo(x):
    print(f"({x})", end=' ')
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)

fibo(6)
print()

'''8-4. Fibonacci(Bottom-up)'''
d = [0] *100

d[1], d[2] = 1, 1
n = 99

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]
print(d[n])