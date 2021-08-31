def solution(clothes):
    my_dict = {}
    for clothe in clothes:
        if clothe[1] not in my_dict:
            my_dict[clothe[1]] = 0
        my_dict[clothe[1]] += 1

    my_list = list(my_dict.values())
    answer = 1
    for a in my_list:
        answer *= (a+1)
        
    return answer-1

print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))