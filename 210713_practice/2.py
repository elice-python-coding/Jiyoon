#카카오특 신규 아이디 추천
# https://programmers.co.kr/learn/courses/30/lessons/72410?language=python3

def solution(new_id):
    new_id = new_id.lower()

    new_id = ''.join([c for c in new_id if c.islower() or c.isdigit() or c in ['-', '_', '.']])

    while '..' in new_id:
        new_id = new_id.replace('..', '.')

    new_id = new_id.strip('.')

    new_id = new_id if new_id else "a"

    new_id = new_id[:15].strip('.') # 글자가 15자가 안되어도 ok

    while len(new_id) <= 2:
        new_id += new_id[-1]

    return new_id


print(solution('1'))