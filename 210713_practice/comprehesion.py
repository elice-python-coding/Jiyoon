# 1) 1 ~ 10을 담는 리스트를 만들자
_list = []
for i in range(1, 11):
        _list.append(i)

# expression for commponent in input_sequence <if statement>
_list = [num for num in range(1, 11)]


# 2) 2, 4, ..., 20
_list = []
for i in range(1, 11):
        _list.append(i * 2)

_list = [num * 2 for num in range(1, 11)]


# 3) 주어진 리스트를 받아서 3의 배수만 저장
ref = [23, 42, 15, 67, 83, 81]

_list = []
for num in ref:
    if num % 3 == 0:
        _list.append(num)

_list = [num for num in ref if num % 3 == 0]


# 4) 값이 두 개인 튜플을 담은 리스트 받아서 값을 뒤집어서 저장
tup = [(2, 3), (1, 4), (5, 6), (6, 1), (2, 7)]

_list = []
for a, b in tup:
    _list.append((b, a))

_list = [(b, a) for a, b in tup]


# 5) 주어진 리스트를 그대로 담되, 15가 넘는 값은 15로 저장
ref = [2, 4, 16, 15, 13, 12, 11, 16, 14]

_list = []
for num in ref:
    if num >15:
        _list.append(15)
    else:
        _list.append(num)

_list = [num if num <= 15 else 15 for num in ref]
# 삼항 연산자는 elif를 쓸 순 있지만(if 중첩문) 복잡하니까 잘 쓰지 않는다.




