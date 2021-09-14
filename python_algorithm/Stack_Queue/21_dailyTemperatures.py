'''21. 일일 온도'''

# 스택 값 비교
class Solution:
    def dailyTemperatures(self, T):
        answer = [0] * len(T)
        stack = []
        for i, cur in enumerate(T):
            while stack and cur > T[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)

        return answer

# 로컬 확인용 코드
if __name__ == '__main__':
    T = list(map(int, input().split()))
    ans = Solution().dailyTemperatures(T)
    print(ans)
            