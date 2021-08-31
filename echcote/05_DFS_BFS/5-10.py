'''
5-10.py 음료수 얼려먹기
'''
N, M = map(int, input().split())
data = []
for i in range(N):
    data.append(list(map(int, input())))

def dfs(x, y):
    # 주어진 행렬의 크기를 벗어나면 종료
    if x<0 or y<0 or x>=N or y >=M:
        return False
    # 현재 노드를 방문하지 않았다면 방문처리
    if data[x][y] == 0:
        data[x][y] = 1

        # 상하좌우도 재귀 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True

    # 노드를 하나도 방문하지 못한 경우 (원래 벽이거나 이미 방문한 노드)
    return False   

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(N):
    for j in range(M):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result +=1

print(result)