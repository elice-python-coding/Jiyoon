'''20. 유효한 괄호'''

# 내 풀이
class Solution:
    def isValid(self, s: str) -> bool:
        table = {
            ')': '(',
            '}': '{',
            ']': '['
        }        
        
        stack = []
        for char in s:
            if char not in table:
                stack.append(char)
            elif stack:
                tmp = stack.pop()
                if table[char] != tmp:
                    return False
            else:
                return False
        if stack:
            return False
        return True

    def isValid1(self, s: str) -> bool:
        stack = []
        table = {
            ')': '(',
            '}': '{',
            ']': '['
        } 

        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False
        return len(stack) == 0

# 로컬 확인용 코드
if __name__ == '__main__':
    s = input()
    ans = Solution().isValid(s)
    print(ans)