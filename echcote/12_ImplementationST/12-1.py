'''
럭키 스트레이트
'''

N = list(map(int, input()))

mid = len(N)//2

left = sum(N[:mid])
right = sum(N[mid:])

if left == right:
    print("LUCKY")
else:
    print("READY")