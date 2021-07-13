# elice k번째 수 찾기

def findKth(myInput, k):
#sorted -> 현재 iterable한 데이터를 정렬한 결과를 반환(리스트는 그대로)

    return [-1 if idx < k-1 else sorted(myInput[:idx+1])[k-1] for idx in range(len(myInput))]

# 1. 갯수가 충분히 적으니까 정렬을 매번해도 되겠다.
# 2. idx라는 변수를 0 ~ 최대 길이까지 올려보자.
# 3. 그러면 idx랑 k랑 비교해서 출력하면 되겠다.

# 그냥 이렇게 풀 수도 있다~ 정도로 생각하면 될 듯

# 아래에 코드를 한 줄로 쓴 것과 같다.
result = []
for idx in range(len(myInput)):
    if idx < k-1:
        result.append(-1)
    else:
        tmp_arr = sorted(myInput[:idx+1])
        result.append(tmp.arr[k-1])