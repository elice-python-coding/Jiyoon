def solution(numbers):
    numbers.sort(key = lambda x:(x[0], x[1]))
    answer=''.join(numbers)
    return answer

print(solution([6, 10, 2]))