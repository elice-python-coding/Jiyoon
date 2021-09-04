'''문자열 뒤집기'''

# 내풀이
def reverse_string(string):
    string.reverse()

# 투 포인터를 이용한 스왑
def reverseString1(s) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

# 파이썬다운 방식(Pythonic way)
def reverseString2(s) -> None:
    s.reverse()

    # reverse() 는 리스트에만 제공.
    # 문자열은 슬라이싱을 사용할 수 있다.
    s = s[::-1]

    # 그러나 리트코드에서는 오류가 발생한다.
    s = s[::-1]

if __name__ == "__main__":
    s = ["H", "e", "l", "l", "o"]
    reverseString2(s)
    print(s)